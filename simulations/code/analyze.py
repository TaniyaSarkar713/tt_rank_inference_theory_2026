"""Tables, vector figures and a source/plot-data workbook from actual outputs."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from plot_utils import plt,PALETTE,MARKERS,style
ROOT=Path(__file__).resolve().parents[2]; SIM=ROOT/'simulations'; FIG=ROOT/'paper/figures'
D=pd.concat([pd.read_csv(SIM/'results'/x/'summary.csv') for x in ('study','asymptotic')],ignore_index=True)
D.to_csv(SIM/'results/all_summary.csv',index=False)
profiles=['four_slack','four_two_blocks','three_product','four_three_blocks','six_singular','four_product']
labels={'four_slack':'q=1, p=16','four_two_blocks':'q=2, p=16','three_product':'q=3, p=8',
        'four_three_blocks':'q=3, p=16','six_singular':'q=3, p=64 (singular)','four_product':'q=4, p=16'}
slopes=[]
for profile in profiles:
    g=D[(D.family=='classification')&(D.profile==profile)&(D.method=='graded')].sort_values('n')
    early=g[g.n<=8192];late=g[g.n>=131072]
    m=float(np.polyfit(np.log(late.n),np.log(late.mean_length),1)[0]);
    se=float(np.sqrt(np.sum((late.length_mcse/late.mean_length)**2))/np.log(late.n.max()/late.n.min()))
    slopes.append(dict(profile=profile,q=int(g.q.iloc[0]),p=int(g.p.iloc[0]),theory=-float(g.q.iloc[0])/2,
                       primary_slope=np.polyfit(np.log(early.n),np.log(early.mean_length),1)[0],late_slope=m,late_slope_mcse=se))
S=pd.DataFrame(slopes);S.to_csv(SIM/'results/slopes.csv',index=False)
# Figure 1: the prespecified four-way local path, shown before algorithm details.
fig,axes=plt.subplots(1,2,figsize=(7,3.8))
methods=['graded','ambient','known_rank_wald','selected_rank_wald_k2','degree_wald']
names=['Graded honest','Ambient scalar','Known-rank Wald','Selected-rank Wald (2)','Boundary-degree Wald']
for ax,lname,title in zip(axes,['tangent','normal'],['(a) Tangent-aligned loading','(b) Nearly normal loading']):
    for j,(method,label) in enumerate(zip(methods,names)):
        g=D[(D.family=='activation')&(D.n==2048)&(D.loading==lname)&(D.method==method)].sort_values('c')
        # Small displacements along x make overlapping error bars visible.
        x=g.weak_bond/(.2/np.sqrt(2048))
        ax.errorbar(x,g.coverage,yerr=np.maximum(0,np.array([g.coverage-g.coverage_lo,g.coverage_hi-g.coverage])),color=PALETTE[j],marker=MARKERS[j],linestyle=['-','--','-.',':','--'][j],label=label,capsize=2)
    ax.axhline(.95,color='gray',lw=.8);ax.set_ylim(0,1.04);ax.set_xlabel(r'Central bond $\tau_2/(\sigma/\sqrt{n})$');ax.set_title(title);style(ax)
axes[0].set_ylabel('Coverage probability');fig.legend(*axes[1].get_legend_handles_labels(),loc='lower center',ncol=3,frameon=False,bbox_to_anchor=(.5,-.01))
fig.tight_layout(rect=(0,.14,1,1));fig.savefig(FIG/'activation.pdf',bbox_inches='tight');plt.close(fig)
# Figure 2: mean length and late effective slopes.
fig,axes=plt.subplots(1,2,figsize=(7,3.8))
for j,profile in enumerate(profiles):
    g=D[(D.family=='classification')&(D.profile==profile)&(D.method=='graded')].sort_values('n')
    axes[0].errorbar(g.n,g.mean_length,yerr=1.96*g.length_mcse,color=PALETTE[j],marker=MARKERS[j],label=labels[profile])
    nn=g.n.to_numpy();ll=g.mean_length.to_numpy();eff=np.diff(np.log(ll))/np.diff(np.log(nn));mid=np.sqrt(nn[:-1]*nn[1:])
    axes[1].plot(mid,eff,color=PALETTE[j],marker=MARKERS[j],label=labels[profile])
axes[0].set_xscale('log');axes[0].set_yscale('log');axes[0].set_ylabel('Mean interval length (log scale)')
axes[1].set_xscale('log');axes[1].set_ylabel('Adjacent log-length / log-n slope')
for q in (1,2,3,4):axes[1].axhline(-q/2,color='gray',linestyle=':',linewidth=.7)
for ax in axes:ax.set_xlabel('Sample size n (log scale)');style(ax)
axes[0].set_title('(a) Graded confidence intervals');axes[1].set_title('(b) Approach to predicted exponents')
axes[1].set_xlabel('Geometric midpoint of adjacent n (log)')
fig.legend(*axes[0].get_legend_handles_labels(),loc='lower center',ncol=3,frameon=False,bbox_to_anchor=(.5,-.01))
fig.tight_layout(rect=(0,.15,1,1));fig.savefig(FIG/'rates.pdf',bbox_inches='tight');plt.close(fig)
# Figure 3: length at the exact point and coverage under allowed departure.
fig,axes=plt.subplots(1,2,figsize=(7,3.8))
for j,(method,name) in enumerate([('graded','Exact-model graded'),('tube_graded','Tube-aware graded'),('ambient','Ambient scalar'),('degree_wald','Boundary-degree Wald')]):
    for ax,depart,metric in [(axes[0],False,'mean_length'),(axes[1],True,'coverage')]:
        g=D[(D.family=='tube')&(D.n==2048)&(D.eta>0)&(D.departure==depart)&(D.method==method)].sort_values('eta')
        x=g.eta/(.2/np.sqrt(2048))
        err=1.96*g.length_mcse if metric=='mean_length' else np.maximum(0,np.array([g.coverage-g.coverage_lo,g.coverage_hi-g.coverage]))
        ax.errorbar(x,g[metric],yerr=err,color=PALETTE[j],marker=MARKERS[j],linestyle=['-','--','-.',':'][j],label=name,capsize=2)
axes[0].set_yscale('log');axes[0].set_ylabel('Mean length at exact $B_0$ (log)');axes[0].set_title('(a) Cost of the known allowance')
axes[1].set_ylim(0,1.04);axes[1].axhline(.95,color='gray',lw=.8);axes[1].set_ylabel(r'Coverage at $B_0+\eta A$');axes[1].set_title('(b) Consequence of ignoring it')
for ax in axes:ax.set_xscale('log');ax.set_xlabel(r'$\eta/(\sigma/\sqrt{n})$ (log scale)');style(ax)
fig.legend(*axes[0].get_legend_handles_labels(),loc='lower center',ncol=2,frameon=False,bbox_to_anchor=(.5,-.01))
fig.tight_layout(rect=(0,.14,1,1));fig.savefig(FIG/'tube.pdf',bbox_inches='tight');plt.close(fig)
# Compact manuscript table: actual measured slopes and Monte Carlo error.
lines=[r'\begin{tabular}{lrrrr}',r'\toprule',r'Profile & $p$ & Predicted & Primary & Large-$n$ (MCSE) \\',r'\midrule']
texnames={'four_slack':'Four-mode slack','four_two_blocks':'Four-mode two blocks','three_product':'Three-mode product','four_three_blocks':'Four-mode three blocks','six_singular':'Six-mode singular','four_product':'Four-mode product'}
for _,r in S.iterrows():
    exp=int(np.floor(np.log10(r.late_slope_mcse)))
    mcse_text=(f"${r.late_slope_mcse/10**exp:.1f}"+r"\times10^{"+str(exp)+"}$" if r.late_slope_mcse<1e-4 else f"{r.late_slope_mcse:.3f}")
    lines.append(f"{texnames[r.profile]} & {int(r.p)} & {r.theory:.2f} & {r.primary_slope:.3f} & {r.late_slope:.3f} ({mcse_text}) " + chr(92)*2)
lines += [r'\bottomrule',r'\end{tabular}'];(ROOT/'paper/sections/slopes_table.tex').write_text('\n'.join(lines)+'\n')
# Workbook contains every input summary used in plots, not only selected panels.
nov=pd.read_csv(ROOT/'literature/novelty_matrix.csv');settings=[]
for study in ('study','asymptotic'):
    meta=json.loads((SIM/'results'/study/'metadata.json').read_text())
    for c in meta['settings']:
        c=dict(c);c['study']=study;c['seed']=meta['seed'];c['replicates']=meta['reps'];c['raw_file']=f'simulations/results/{study}/replicates_{c["id"]:03d}.csv.gz';settings.append(c)
settings=pd.DataFrame(settings);settings['dims']=settings.dims.astype(str);settings['caps']=settings.caps.astype(str)
notes=pd.DataFrame([
 ('Coverage','Proportion; Wilson95% intervals; no MCSE-zero interpretation as certainty.'),
 ('Mean length','Coefficient-functional units; arithmetic replicate mean; length_mcse=sample SD/sqrt(2000).'),
 ('Slope','Log(mean length) difference divided by log(n) difference for the two largest n; delta-method MCSE from independent settings.'),
 ('Sources','Simulation input settings and seed are in Settings; raw interval records at the relative raw_file paths. All plotted values are in Summary.'),
 ('Novelty','Primary source URLs and verification locators in Novelty; absence of overlap is not certified novelty.'),
 ('Addendum','n=131072 and2097152 added after seeing finite-n slope transients; no tuning or method change.')],columns=['field','definition'])
with pd.ExcelWriter(ROOT/'research_companion.xlsx',engine='openpyxl') as writer:
    for name,frame in [('Summary',D),('Slopes',S),('Settings',settings),('Novelty',nov),('Readme',notes)]:
        frame.to_excel(writer,sheet_name=name,index=False);ws=writer.sheets[name];ws.freeze_panes='A2';ws.auto_filter.ref=ws.dimensions
        for column in ws.columns:
            length=min(65,max(12,max(len(str(c.value or '')) for c in list(column)[:40])+2));ws.column_dimensions[column[0].column_letter].width=length
# Analysis report with exact machine-derived summaries.
rep=['# Empirical findings','',f'{len(settings)*2000:,} independent datasets; {len(settings)} settings; {len(D)} method/functional summary rows.','', '## Rate checks','',S.to_markdown(index=False),'','The large-n slopes use a transparent post-primary addendum. Their Monte Carlo errors account for simulation means, not asymptotic approximation bias.','', '## Pointwise versus local coverage','']
sub=D[(D.family=='activation')&(D.n==2048)&(D.loading=='normal')&(D.method.isin(['graded','degree_wald','known_rank_wald','selected_rank_wald_k2']))]
rep.append(sub[['c','method','coverage','coverage_mcse','coverage_lo','coverage_hi','mean_length']].to_markdown(index=False))
rep+=['','## Structural departure','']
sub=D[(D.family=='tube')&(D.n==2048)&D.departure&(D.method.isin(['graded','tube_graded','ambient']))]
rep.append(sub[['eta_kind','eta','method','coverage','coverage_mcse','mean_length']].to_markdown(index=False))
rep+=['','## Limits','', 'All graded intervals covered in the main exactly specified contact experiments. At 2000/2000, the Wilson interval is approximately [0.9981,1]; this documents conservatism and does not prove population coverage one. The narrow degree-calibrated intervals are pointwise benchmarks with poor local coverage. Neither their short width nor the conservative method’s coverage proves efficient constants. Stress diagnostics outside Gaussian homoskedastic errors do not establish robustness.']
(SIM/'results/analysis.md').write_text('\n'.join(rep)+'\n')
print('Generated three vector figures, 705-row combined summary, slopes, analysis, and workbook.')
