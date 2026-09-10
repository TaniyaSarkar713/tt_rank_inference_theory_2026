"""Assemble dated theory revision without rewriting the historical manuscript."""
from pathlib import Path
import os
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def typeset_note(content):
    """Convert development-note inline symbols to math without changing formulas.

    Display math is already TeX. Inline development expressions have no spaces;
    translate them tokenwise, preserving their exact order and all punctuation.
    """
    symbols = dict(zip('αβγδθεκλμξρστΦΘΣΔΩ',
                       ['alpha','beta','gamma','delta','theta','epsilon','kappa',
                        'lambda','mu','xi','rho','sigma','tau','Phi','Theta','Sigma','Delta','Omega']))
    symbols.update({'≤':'le','≥':'ge','∈':'in','⊗':'otimes','×':'times','∼':'sim',
                    '≍':'asymp','≪':'ll','≫':'gg','≲':'lesssim','→':'to','∏':'prod',
                    '∅':'varnothing','∎':'blacksquare','〈':'langle','〉':'rangle',
                    '⊥':'perp','∞':'infty','χ':'chi','η':'eta','ω':'omega','ψ':'psi'})
    symbols['Σ']='sum'
    def token(match):
        raw=match.group(0)
        if not re.search(r'[_^=≤≥∈⊗×∼≍≪≫≲→∏∅∎〈〉⊥∞√αβγδθεκλμξρστΦΘΣΔΩχηωψ²³⁴]',raw):
            return raw
        if raw.startswith('#') or raw.startswith('http') or '](' in raw:
            return raw
        end=''
        while raw and raw[-1] in '.,;:':
            end=raw[-1]+end;raw=raw[:-1]
        # Escape set braces; preserve TeX-style subscript and exponent groups.
        stack=[];chars=[]
        for i,ch in enumerate(raw):
            if ch=='{':
                group=i>0 and raw[i-1] in '_^√'
                stack.append(group);chars.append('{' if group else r'\{')
            elif ch=='}':
                group=stack.pop() if stack else False
                chars.append('}' if group else r'\}')
            else:chars.append(ch)
        value=''.join(chars).replace('−','-').replace('²','^{2}').replace('³','^{3}').replace('⁴','^{4}').replace('ᵀ','^T')
        value=value.replace('B̃',r'\widetilde B')
        value=value.replace('||',r'\|')
        value=''.join(('\\'+symbols[ch]+' ') if ch in symbols else ch for ch in value)
        value=re.sub(r'_(op|min|max|old|new|cert|MC)(?![A-Za-z])',r'_{\1}',value)
        value=re.sub(r'√([A-Za-z](?:_[0-9A-Za-z])?)',r'\\sqrt{\1}',value)
        value=value.replace('√',r'\sqrt ')
        value=re.sub(r'\b(log|exp|diag|rank|span|dist|binom)\b',r'\\operatorname{\1}',value)
        value=re.sub(r'\^\[([^\]]+)\]',r'^{[\1]}',value)
        return '$'+value.strip()+'$'+end
    blocks=re.split(r'(\\\[[\s\S]*?\\\])',content)
    for i in range(0,len(blocks),2):
        blocks[i]=re.sub(r'(?:\{[^{}]*\}|\S)+',token,blocks[i])
    return ''.join(blocks)


def main():
    cache = Path('/tmp/tt_revision_texcache')
    cache.mkdir(exist_ok=True)
    tex_env = dict(os.environ, TEXMFCACHE=str(cache), TEXMFVAR=str(cache))
    text = (HERE / 'frontmatter.md').read_text()
    notes = [
        ('A. Rank-two geometry and the single-unfolding comparison', 'active_rank_two_modulus.md'),
        ('B. General normal-loading geometry', 'general_normal_modulus.md'),
        ('C. Selected-cross inference and calibration', 'certified_cross_inference.md'),
        ('D. Learned mode compression', 'growing_dimension_general_tt.md'),
        ('E. Minimum-distance calibration: established and partial results',
         'certified_minimum_distance_calibration.md'),
    ]
    for title, name in notes:
        content = (ROOT / 'theory' / name).read_text()
        content = content.split('\n', 1)[1]
        if name == 'active_rank_two_modulus.md':
            content = content[content.index('## 1.'):content.index('## 5.')]
            content = content.replace('Fix tensor order K≥3', 'Fix 0<α<1/2 and tensor order K≥3')
            start=content.index('\\[\n \\Theta_2=')
            finish=content.index('\\]',start)
            block=content[start:finish+2].replace('\\[','\\[\n \\begin{gathered}',1)
            block=block.replace('\\},\\qquad\n', '\\},\\\\\n',1)
            block=block.replace('\\]','\\end{gathered}\n\\]')
            content=content[:start]+block+content[finish+2:]
        # Source lists are retained in the development notes; the manuscript has
        # an integrated bibliography and an explicit related-work section.
        for marker in ('## Sources', '## Prior art and proof dependencies'):
            content = content.split(marker)[0]
        content = content.replace('the audited rank-two note', 'Appendix A')
        content = content.replace('the audited rank-two proof', 'Appendix A')
        content = content.replace('the rank-two note', 'Appendix A')
        content = re.sub(r'^## ', '## ', content, flags=re.M)
        text += '\n\n\\newpage\n\n# ' + title + '\n\n' + typeset_note(content.strip()) + '\n'
    (HERE / 'main.md').write_text(text)
    (HERE / 'references.bib').write_text((ROOT / 'paper' / 'references.bib').read_text()
                                       + '\n' + (HERE / 'references_additions.bib').read_text())
    common = ['pandoc', 'main.md', '--from=markdown+tex_math_single_backslash',
              '--standalone', '--citeproc', '--bibliography=references.bib',
              '--number-sections', '--variable=linestretch:1.08',
              '--include-in-header=preamble.tex']
    subprocess.run(common + ['--to=latex', '--output=main.tex'], cwd=HERE, check=True)
    # Compile the saved source itself, preserving diagnostics for inspection.
    for _ in range(3):
        with (HERE / 'compile_output.txt').open('w') as output:
            subprocess.run(['lualatex', '-interaction=nonstopmode', '-halt-on-error', 'main.tex'],
                           cwd=HERE, env=tex_env, stdout=output, stderr=subprocess.STDOUT, check=True)
    print(HERE / 'main.pdf')


if __name__ == '__main__':
    main()
