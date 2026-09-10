"""Validate every stored interval and produce theory-linked summaries/figures."""
import hashlib,json
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import norm

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'simulations'/'results'/'tt_revision_2026_09_09'
FIG=ROOT/'simulations'/'figures'/'tt_revision_2026_09_09'


def main():
    metadata=json.loads((OUT/'metadata.json').read_text()); df=pd.read_csv(OUT/'summary.csv')
    paired=[]; N=metadata['replications_per_setting']; methods=df.method.unique()
    for spec in metadata['settings']:
        idx=spec['setting']; path=OUT/f'setting_{idx:02}.npz'
        assert hashlib.sha256(path.read_bytes()).hexdigest()==spec['sha256']
        with np.load(path) as d:
            psi=float(d['psi'])
            for method in methods:
                lo,hi=d[method+'_lower'],d[method+'_upper']
                length=hi-lo; cover=(lo<=psi)&(psi<=hi)
                row=df[(df.setting==idx)&(df.method==method)].iloc[0]
                assert np.isclose(length.mean(),row.mean_length)
                assert np.isclose(cover.mean(),row.coverage)
                assert np.isclose(length.std(ddof=1)/np.sqrt(N),row.length_mcse)
                if method!='scalar_t':assert np.all(cover[d['ball_covered']])
            old=d['cross_separate_upper']-d['cross_separate_lower']
            new=d['cross_joint_upper']-d['cross_joint_lower']
            assert np.all(new<=old+1e-12)
            ratio=new.mean()/old.mean()
            # Paired influence-function standard error for a ratio of means.
            influence=(new-ratio*old)/old.mean()
            paired.append(dict(setting=idx,n=spec['n'],family=spec['family'],b=spec['b'],
                ratio=ratio,ratio_mcse=influence.std(ddof=1)/np.sqrt(N),
                mean_difference=(new-old).mean(),difference_mcse=(new-old).std(ddof=1)/np.sqrt(N)))
    paired=pd.DataFrame(paired);paired.to_csv(OUT/'paired_comparisons.csv',index=False)
    slopes=[]
    for method in ('cross_separate','cross_joint'):
        v=df[(df.family=='fixed_bond')&(df.method==method)].sort_values('n')
        x=np.log(v.n.to_numpy()); w=(x-x.mean())/np.sum((x-x.mean())**2)
        slope=float(w@np.log(v.mean_length.to_numpy()))
        mcse=float(np.sqrt(np.sum((w*v.length_mcse.to_numpy()/v.mean_length.to_numpy())**2)))
        slopes.append(dict(method=method,slope=slope,mcse=mcse))
    pd.DataFrame(slopes).to_csv(OUT/'slopes.csv',index=False)
    FIG.mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,
                         'pdf.fonttype':42,'savefig.bbox':'tight'})
    fig,axes=plt.subplots(1,2,figsize=(10,3.7))
    styles={'cross_separate':('#555555','o','Separate error bounds'),
            'cross_joint':('#0072B2','s','Joint error budget'),
            'scalar_t':('#D55E00','^','Scalar t interval')}
    for name,(color,marker,label) in styles.items():
        v=df[(df.n==8192)&(df.family=='boundary')&(df.method==name)].sort_values('bond_over_tn')
        axes[0].plot(v.bond_over_tn,v.mean_length/(.2/np.sqrt(8192)),color=color,marker=marker,label=label)
        axes[1].errorbar(v.bond_over_tn,v.coverage,
                        yerr=np.array([v.coverage-v.coverage_low,v.coverage_high-v.coverage]).clip(0),
                        color=color,marker=marker,capsize=2)
    axes[0].set(xscale='symlog',yscale='log',xlabel=r'$b/t_n$',ylabel=r'Mean length / $t_n$')
    axes[0].legend(frameon=False,fontsize=8)
    axes[1].set(xscale='symlog',xlabel=r'$b/t_n$',ylabel='Coverage',ylim=(.935,1.005))
    axes[1].axhline(.95,color='black',ls='--',lw=.8)
    fig.tight_layout();fig.savefig(FIG/'weak_bond.pdf');fig.savefig(FIG/'weak_bond.png',dpi=160);plt.close(fig)
    selected=df[(df.n==8192)&(df.family=='boundary')&df.method.isin(['cross_joint','scalar_t'])][
        ['bond_over_tn','method','coverage','coverage_mcse','mean_length','length_mcse','mean_length_over_scale']]
    note=f'''# Selected-cross simulation findings

There are {metadata['independent_datasets']:,} independent Gaussian regression sufficient-statistic realizations, {N:,} per setting, and {metadata['interval_records']:,} interval records. The ambient embedding has p={metadata['ambient_p']:,}, while only m={metadata['m']} selected features enter inference. The full ambient design is not materialized: Wishart/normal/chi-square sampling exactly reproduces the sufficient-statistic law of the specified regression. This demonstrates the prespecified-coordinate theorem, not adaptation to unknown orientations.

At nominal 95% coverage, 5,000 replications give coverage Monte Carlo SE {np.sqrt(.95*.05/N):.5f} (about 0.31 percentage points). All-success rows have plug-in MCSE zero but a nontrivial Wilson lower limit. Conditional common-ball coverage and dataset-wise length dominance were checked for every stored interval.

{selected.to_markdown(index=False,floatfmt='.6g')}

## Paired length ratios

{paired.to_markdown(index=False,floatfmt='.6g')}

## Fixed-bond slopes

{pd.DataFrame(slopes).to_markdown(index=False,floatfmt='.6g')}

The limiting prediction is −2 for K=4 and fixed b. Finite-grid slopes and their Monte Carlo errors do not remove finite-sample bias. Coverage remains conservative for the cross intervals; the numerator optimization certifies shorter intervals but does not solve optimal expected-length calibration. No unknown-orientation pilot or nonzero-target minimum-distance method was tested.
'''
    (OUT/'analysis.md').write_text(note)
    validation=dict(settings=len(metadata['settings']),independent_datasets=metadata['independent_datasets'],
                    interval_records=metadata['interval_records'],all_hashes_verified=True,
                    raw_summaries_verified=True,all_common_ball_inclusions=True,
                    all_joint_lengths_no_greater=True,max_numerator_bracket_gap=max(
                        x['max_numerator_bracket_gap'] for x in metadata['settings']))
    (OUT/'validation.json').write_text(json.dumps(validation,indent=2)+'\n')
    print(json.dumps(validation,indent=2));print(pd.DataFrame(slopes).to_string(index=False))


if __name__=='__main__':main()
