import matplotlib.pyplot as plt

from ema_workbench import ema_logging, load_results
from ema_workbench.analysis.plotting import kde_over_time

ema_logging.log_to_stderr(ema_logging.INFO)

fn = r'./data/500 gass cases no policy.tar.gz'
experiments, outcomes = load_results(fn)

# the plotting functions return the figure and a dict of axes
fig, axes = kde_over_time(experiments, outcomes, outcomes_to_show=['NG Production capacity',
                                                         'H2 Production capacity'], log=True)
plt.show()