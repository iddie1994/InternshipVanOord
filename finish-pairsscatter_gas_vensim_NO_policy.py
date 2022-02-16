import matplotlib.pyplot as plt

from ema_workbench import ema_logging, load_results
from ema_workbench.analysis import Density
from ema_workbench.analysis.pairs_plotting import (pairs_scatter)

from ema_workbench.analysis.pairs_plotting import (pairs_lines, pairs_scatter,
                                                   pairs_density)

ema_logging.log_to_stderr(ema_logging.INFO)

file_name = r'./data/windhydrogen.tar.gz'
experiments, outcomes = load_results(file_name)

# the plotting functions return the figure and a dict of axes
fig, axes =  pairs_lines(experiments,
                  outcomes, density=Density.VIOLIN)
fig.set_figheight(6)
fig.set_figwidth(12)

plt.show()

# import seaborn as sns
#
# ema_logging.log_to_stderr(ema_logging.INFO)
#
# file_name = r'./data/100 gas cases no policy.tar.gz'
# experiments, outcomes = load_results(file_name)
#
# df = pd.DataFrame.from_dict(outcomes)
# df = df.assign(policy=experiments['policy'])
#
# # rename the policies using numbers
# df['policy'] = df['policy'].map({p: i for i, p in
#                                  enumerate(set(experiments['policy']))})
#
# # use seaborn to plot the dataframe
# grid = sns.pairplot(df, hue='policy', vars=outcomes.keys())
# ax = plt.gca()
# plt.show()