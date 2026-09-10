import os
from pathlib import Path
os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2]/"build/matplotlib"))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
PALETTE=['#0072B2','#D55E00','#009E73','#CC79A7','#E69F00','#333333']
MARKERS=['o','s','^','D','v','x']
plt.rcParams.update({'font.family':'serif','font.size':10,'axes.labelsize':10,
 'axes.titlesize':10,'legend.fontsize':9,'xtick.labelsize':9,'ytick.labelsize':9,
 'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42,
 'lines.linewidth':1.5,'lines.markersize':4})
def style(ax):ax.grid(alpha=.17,linewidth=.5)
