"""Reaggregate audit replicates; retain primary analysis and workbook intact."""
from pathlib import Path
import hashlib,json
import numpy as np
import pandas as pd
from scipy.stats import norm
from plot_utils import plt,PALETTE,MARKERS,style
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'simulations/results/audit'

def main():
    plt.rcParams.update({'font.size':12,'axes.labelsize':12,'axes.titlesize':10.5,'legend.fontsize':10.5,'xtick.labelsize':10.5,'ytick.labelsize':10.5})
    meta=json.loads((OUT/'metadata.json').read_text())
    for f,h in meta['code_hashes'].items():
        assert hashlib.sha256((ROOT/'simulations/code'/f).read_bytes()).hexdigest()==h
    frames=[pd.read_csv(f) for f in sorted(OUT.glob('replicates_n*.csv.gz'))]
    df=pd.concat(frames,ignore_index=True);assert len(df)==210000
    assert np.array_equal(df.covered,(df.lower<=df.target)&(df.target<=df.upper))
    assert np.allclose(df.length,df.upper-df.lower,rtol=1e-11,atol=1e-15)
    assert (df.length>=0).all()
    rows=[];z=norm.ppf(.975)
    for (n,kappa,method),g in df.groupby(['n','kappa','method']):
        N=len(g);assert N==2000;assert g.rep.nunique()==N;phat=g.covered.mean()
        denom=1+z*z/N;mid=(phat+z*z/(2*N))/denom
        whalf=z*np.sqrt(phat*(1-phat)/N+z*z/(4*N*N))/denom
        rows.append({'n':n,'kappa':kappa,'method':method,'reps':N,'epsilon':g.epsilon.iloc[0],
                     'coverage':phat,'coverage_mcse':np.sqrt(phat*(1-phat)/N),
                     'wilson_lower':mid-whalf,'wilson_upper':mid+whalf,
                     'mean_length':g.length.mean(),'length_mcse':g.length.std(ddof=1)/np.sqrt(N),
                     'rate_scale':g.rate_scale.iloc[0],'pure_cubic_scale':g.pure_cubic_scale.iloc[0],
                     'fallback_rate':g.fallback.mean(),'empty_rate':g['empty'].mean()})
    summary=pd.DataFrame(rows);summary['length_over_rate']=summary.mean_length/summary.rate_scale
    pairs=[]
    for (n,kappa),g in df.groupby(['n','kappa']):
        for old,new,label in [('original','energy','known'),('original_unknown','energy_unknown','unknown')]:
            a=g[g.method==old].sort_values('rep').length.to_numpy()
            b=g[g.method==new].sort_values('rep').length.to_numpy()
            assert (b<=a+1e-13).all()
            ratio=b.mean()/a.mean();influence=(b-ratio*a)/a.mean()
            pairs.append({'n':n,'kappa':kappa,'noise':label,'mean_length_ratio':ratio,
                          'ratio_mcse':influence.std(ddof=1)/np.sqrt(len(a)),
                          'mean_length_reduction':(a-b).mean(),
                          'reduction_mcse':(a-b).std(ddof=1)/np.sqrt(len(a))})
    pairs=pd.DataFrame(pairs);summary.to_csv(OUT/'summary.csv',index=False);pairs.to_csv(OUT/'paired_comparison.csv',index=False)
    fig,axes=plt.subplots(1,2,figsize=(8.2,3.8),layout='constrained')
    for i,n in enumerate(meta['n']):
        g=summary[(summary.n==n)&(summary.method=='energy')].sort_values('kappa')
        axes[0].errorbar(g.kappa,g.length_over_rate,yerr=z*g.length_mcse/g.rate_scale,label=f'n = {n:,}',color=PALETTE[i],marker=MARKERS[i],capsize=2)
        h=pairs[(pairs.n==n)&(pairs.noise=='known')].sort_values('kappa')
        axes[1].errorbar(h.kappa,h.mean_length_ratio,yerr=z*h.ratio_mcse,color=PALETTE[i],marker=MARKERS[i],capsize=2)
    for ax in axes:
        ax.set_xscale('symlog',linthresh=.1);ax.set_xlabel(r'Loading coefficient multiplier $\kappa$');style(ax)
    axes[0].set_yscale('log');axes[0].set_ylabel(r'Mean energy-interval length / $\mathcal{R}_{A_\epsilon}(t_n)$')
    axes[0].set_title('(a) All-degree loading transition');axes[0].legend(frameon=False)
    axes[1].axhline(1,color='#777777',ls=':',lw=1);axes[1].set_ylim(0,1.04)
    axes[1].set_ylabel('Ratio of mean lengths: energy / original')
    axes[1].set_title('(b) Paired length reduction')
    fig.savefig(ROOT/'paper/figures/audit_transition.pdf');plt.close(fig)
    with pd.ExcelWriter(ROOT/'audit/audit_companion.xlsx',engine='openpyxl') as writer:
        summary.to_excel(writer,sheet_name='Interval summaries',index=False)
        pairs.to_excel(writer,sheet_name='Paired comparison',index=False)
        pd.DataFrame([{'key':k,'value':json.dumps(v)} for k,v in meta.items()]).to_excel(writer,sheet_name='Metadata',index=False)
    selected=summary[(summary.n==8192)&(summary.method.isin(['original','energy','ambient']))&(summary.kappa.isin([0.,1.,100.,10000.]))]
    text='# Post-audit paired experiment\n\n6,000 new independent datasets: three cohorts of 2,000. The seven deterministic loadings and five methods reuse each cohort; they are not independent experiments. Total 210,000 interval records, 105 summary rows. The original 186,000 datasets and primary figures remain unchanged.\n\n'
    text+='The loading is (E1111 + epsilon E1000)/sqrt(1+epsilon²), epsilon=kappa*t_n²/lambda². lambda=3, sigma=.2, caps=(1,2,1), truth=lambda E0000. The proved reference is R_A(t_n)=(epsilon*t_n+t_n³/lambda²)/sqrt(1+epsilon²).\n\n'
    text+=selected[['n','kappa','method','coverage','coverage_mcse','wilson_lower','mean_length','length_mcse','length_over_rate']].to_markdown(index=False,floatfmt='.7g')+'\n\n'
    text+=pairs[(pairs.n==8192)&(pairs.noise=='known')].to_markdown(index=False,floatfmt='.7g')+'\n\n'
    text+='Coverage MCSE is the binomial plug-in standard error; at 2,000/2,000 successes it is zero, so the Wilson interval is also reported and no perfect-population-coverage claim is made. Ratio MCSE uses the paired influence variable (new − ratio*old)/mean(old), preserving within-dataset dependence. Error bars are pointwise Monte Carlo intervals, not simultaneous confidence bands.\n\n'
    text+='The energy certificate reduces length on every replicate, as predicted by the deterministic theorem. Conservative constants remain large. The normalized curves examine the uniform multiscale bound; they do not estimate a sharp minimax constant or prove the theorem. At large kappa the tangent term dominates and the two certificates approach each other. No non-Gaussian optimality claim is assessed by this Gaussian study.\n'
    (OUT/'analysis.md').write_text(text)
    validation={'unique_datasets':int(df[['n','rep']].drop_duplicates().shape[0]),'interval_records':len(df),'summary_rows':len(summary),'paired_comparisons':len(pairs),'all_code_hashes_match':True,'endpoints_coverage_length_verified':True,'all_energy_lengths_no_larger':True}
    (OUT/'validation.json').write_text(json.dumps(validation,indent=2)+'\n');print(json.dumps(validation,indent=2))
    print(pairs[(pairs.n==8192)&(pairs.noise=='known')].to_string(index=False))
if __name__=='__main__':main()
