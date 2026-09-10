from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
from scipy.stats import norm
from plot_utils import plt,PALETTE,MARKERS,style
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'simulations/results/robust_audit'

def main():
    plt.rcParams.update({'font.size':12,'axes.labelsize':12,'axes.titlesize':10.5,'legend.fontsize':10.5,'xtick.labelsize':10.5,'ytick.labelsize':10.5})
    meta=json.loads((OUT/'metadata.json').read_text())
    for f,h in meta['code_hashes'].items():assert hashlib.sha256((ROOT/'simulations/code'/f).read_bytes()).hexdigest()==h
    df=pd.concat([pd.read_csv(f) for f in sorted(OUT.glob('replicates_*.csv.gz'))],ignore_index=True)
    assert len(df)==12000;assert df[['noise','n','rep']].drop_duplicates().shape[0]==6000
    assert np.array_equal(df.covered,(df.lower<=0)&(df.upper>=0));assert np.allclose(df.length,df.upper-df.lower,rtol=1e-11,atol=1e-15)
    assert ((df.ball_covered==0)|(df.covered==1)).all()
    rows=[];z=norm.ppf(.975)
    for (noise,n,q),g in df.groupby(['noise','n','q']):
        N=len(g);assert N==1000;ph=g.covered.mean();denom=1+z*z/N
        half=z*np.sqrt(ph*(1-ph)/N+z*z/(4*N*N))/denom;mid=(ph+z*z/(2*N))/denom
        rows.append({'noise':noise,'n':n,'q':q,'reps':N,'coverage':ph,'coverage_mcse':np.sqrt(ph*(1-ph)/N),'wilson_lower':mid-half,'wilson_upper':mid+half,'mean_length':g.length.mean(),'length_mcse':g.length.std(ddof=1)/np.sqrt(N),'ball_coverage':g.ball_covered.mean(),'mean_radius':g.radius.mean(),'fallback_rate':g.fallback.mean()})
    summary=pd.DataFrame(rows);summary.to_csv(OUT/'summary.csv',index=False);slopes=[]
    fig,axes=plt.subplots(1,2,figsize=(8.2,3.6),layout='constrained')
    for ax,q in zip(axes,[3,4]):
        for i,noise in enumerate(meta['noise']):
            g=summary[(summary.noise==noise)&(summary.q==q)].sort_values('n')
            ax.errorbar(g.n,g.mean_length,yerr=1.96*g.length_mcse,label=noise,color=PALETTE[i],marker=MARKERS[i],capsize=2)
            x=np.log(g.n.to_numpy());y=np.log(g.mean_length.to_numpy());w=(x-x.mean())/sum((x-x.mean())**2)
            slopes.append({'noise':noise,'q':q,'slope':float(w@y),'slope_mcse':float(np.sqrt(sum((w*g.length_mcse.to_numpy()/g.mean_length.to_numpy())**2))),'predicted':-q/2})
        base=summary[(summary.q==q)&(summary.noise=='Gaussian')].sort_values('n').iloc[-1]
        xx=np.array(meta['n']);ax.plot(xx,base.mean_length*(xx/base.n)**(-q/2),ls=':',color='#555555',label=f'slope -{q}/2')
        ax.set_xscale('log',base=2);ax.set_yscale('log');ax.set_xlabel('Sample size n');ax.set_ylabel('Mean interval length');ax.set_title(f'Contact order q = {q}');style(ax);ax.legend(frameon=False)
    fig.savefig(ROOT/'paper/figures/robust_audit.pdf');plt.close(fig)
    slopes=pd.DataFrame(slopes);slopes.to_csv(OUT/'slopes.csv',index=False)
    text='# Finite-variance audit experiment\n\n6,000 new independent datasets in six cohorts. Each cohort has 1,000 replications; the q=3 and q=4 procedures share those observations. There are 12,000 interval records. The t2.5 noise is centered and scaled to variance .2²; it has no finite third or fourth moment. No outliers were artificially labeled and no contamination model is asserted.\n\n'
    text+=summary.to_markdown(index=False,floatfmt='.7g')+'\n\n'+slopes.to_markdown(index=False,floatfmt='.7g')+'\n\n'
    text+='Slopes are finite-sample descriptive fits over n=512,2048,8192, not exact verification of the asymptotic slope. Monte Carlo standard errors account for independent n cohorts; q comparisons are paired. At 1,000/1,000 successes the binomial plug-in MCSE is zero; the Wilson interval, approximately [0.9962,1], expresses uncertainty. The radius has deliberately large fixed-dimension constants, so conservative coverage is expected. The theorem gives worst-noise expected-length order with a known variance bound; these simulations do not establish sharp constants.\n'
    (OUT/'analysis.md').write_text(text)
    (OUT/'validation.json').write_text(json.dumps({'datasets':6000,'interval_records':12000,'all_hashes_match':True,'endpoints_and_common_event_verified':True},indent=2)+'\n')
    print(summary.to_string(index=False));print(slopes.to_string(index=False))
if __name__=='__main__':main()
