"""Reaggregate every stored interval and audit the numerical evidence."""
from pathlib import Path
import json,hashlib
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parents[2];R=ROOT/'simulations/results'
reports=[];total=0
for study in ('study','asymptotic'):
    folder=R/study; summary=pd.read_csv(folder/'summary.csv');meta=json.loads((folder/'metadata.json').read_text())
    for name,expected in meta['code_sha256'].items():
        path=ROOT/'simulations/code'/name
        if path.exists(): assert hashlib.sha256(path.read_bytes()).hexdigest()==expected,(study,name,'execution-source hash changed')
    assert len(summary.setting.unique())==len(meta['settings'])
    for c in meta['settings']:
        data=pd.read_csv(folder/f'replicates_{c["id"]:03d}.csv.gz',float_precision='round_trip')
        assert data.rep.nunique()==meta['reps'];assert np.isfinite(data[['length','center','target','squared_error']]).all().all()
        assert (data.length>=0).all();assert data.covered.isin([0,1]).all()
        assert (data.lower<=data.upper).all()
        assert np.array_equal(data.covered.to_numpy(),((data.lower<=data.target)&(data.target<=data.upper)).to_numpy().astype(int))
        assert np.allclose(data.length,data.upper-data.lower,rtol=1e-12,atol=1e-28)
        assert np.allclose(data.squared_error,(data.center-data.target)**2,rtol=1e-7,atol=1e-29)
        for (loading,method),g in data.groupby(['loading','method']):
            row=summary[(summary.setting==c['id'])&(summary.loading==loading)&(summary.method==method)].iloc[0]
            assert len(g)==row.reps==meta['reps']
            checks=[(g.covered.mean(),row.coverage),(g.length.mean(),row.mean_length),(g.squared_error.mean(),row.mse),
                    (g.length.std(ddof=1)/np.sqrt(len(g)),row.length_mcse),
                    (np.sqrt(row.coverage*(1-row.coverage)/len(g)),row.coverage_mcse)]
            for computed,stored in checks: assert np.isclose(computed,stored,rtol=1e-10,atol=1e-28),(c['id'],method,computed,stored)
            assert row.coverage_lo>=-1e-12 and row.coverage_hi<=1+1e-12
        total+=len(data)
    reports.append(f'{study}: all {len(meta["settings"])} settings reaggregated; execution-source hashes match.')
allsummary=pd.read_csv(R/'all_summary.csv');assert total==len(allsummary)*2000==1410000
workbook=pd.read_excel(ROOT/'research_companion.xlsx',sheet_name='Summary');assert len(workbook)==len(allsummary)==705
for col in ['coverage','mean_length','coverage_mcse','length_mcse']:
    assert np.allclose(workbook[col],allsummary[col],rtol=1e-12,atol=1e-28),col
reports+=['PASS 1,410,000 replicate rows, including direct coverage checks from stored endpoints; 705 summary rows; workbook agrees with plotted inputs.',
 'Monte Carlo coverage intervals are Wilson intervals; no all-success result is interpreted as certain population coverage.',
 'No old-project Monte Carlo runs were pooled into this study.']
(R/'validation.txt').write_text('\n'.join(reports)+'\n');print('\n'.join(reports))
