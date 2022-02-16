import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from ema_workbench import ema_logging, load_results
from ema_workbench.analysis import lines, Density

ema_logging.log_to_stderr(ema_logging.INFO)

file_name = r'./data/12Wind6H2_DoggerBank_AEL_Islandpower_sensitivity3.tar.gz'
# 500 gas cases no policy.tar.gz'
experiments, outcomes = load_results(file_name)

# the plotting functions return the figure and a dict of axes
fig, axes = lines(experiments, outcomes,
                  # outcomes_to_show=[
                  #     # '"Net-present value NG investment"',
                  #                   'NG Production capacity'],
                  density=Density.VIOLIN,  titles=None)
fig.set_figheight(6)
fig.set_figwidth(12)

# we can access each of the axes and make changes
for key, value in axes.items():
    # the key is the name of the outcome for the normal plot
    # and the name plus '_density' for the endstate distribution
    if key.endswith('_density'):
        value.set_xscale('log')


plt.xlabel('Final time NPV')
plt.ylabel('Net present value (b€)')
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d b€'))
plt.show()
