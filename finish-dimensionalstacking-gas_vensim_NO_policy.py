import matplotlib.pyplot as plt
import matplotlib as mpl
from ema_workbench import ema_logging, load_results
from ema_workbench.analysis import dimensional_stacking

ema_logging.log_to_stderr(level=ema_logging.INFO)

# load data
fn = './data/windhydrogen500.tar.gz'
x, outcomes = load_results(fn)

y = outcomes['Cumulative hydrogen production'][:, -1] > 18000

fig = dimensional_stacking.create_pivot_plot(x, y, 2, nbins=3)

plt.show()