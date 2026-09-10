"""Compile LaTeX and bibliography with all generated files inside the project."""
from pathlib import Path
import os,subprocess,shutil
ROOT=Path(__file__).resolve().parents[2]; PAPER=ROOT/'paper';OUT=ROOT/'build/paper';OUT.mkdir(parents=True,exist_ok=True)
env=os.environ.copy();env['BIBINPUTS']=str(PAPER)+os.pathsep+env.get('BIBINPUTS','')
commands=[(['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',f'-output-directory={OUT}','main.tex'],PAPER),
          (['bibtex','main'],OUT),
          (['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',f'-output-directory={OUT}','main.tex'],PAPER),
          (['pdflatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',f'-output-directory={OUT}','main.tex'],PAPER)]
logs=[]
for args,cwd in commands:
    run=subprocess.run(args,cwd=cwd,env=env,capture_output=True,text=True);logs.append(run.stdout+'\n'+run.stderr)
    if run.returncode:
        (ROOT/'build/compile-output.txt').write_text('\n'.join(logs));print(run.stdout[-7000:]);raise SystemExit(run.returncode)
# Float placement can require an additional reference stabilization pass.
for _ in range(3):
    log=(OUT/'main.log').read_text()
    if 'Label(s) may have changed' not in log and 'Rerun to get' not in log: break
    args,cwd=commands[-1];run=subprocess.run(args,cwd=cwd,env=env,capture_output=True,text=True);logs.append(run.stdout+'\n'+run.stderr)
    if run.returncode: print(run.stdout[-5000:]);raise SystemExit(run.returncode)
(ROOT/'build/compile-output.txt').write_text('\n'.join(logs));shutil.copy2(OUT/'main.pdf',PAPER/'main.pdf')
print('Compiled',PAPER/'main.pdf')
print('\n'.join(x for x in (OUT/'main.log').read_text().splitlines() if any(q in x for q in ['Warning','Overfull','Output written'])))
