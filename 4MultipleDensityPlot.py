import math
import matplotlib.pyplot as plt

from ema_workbench import ema_logging, load_results
from ema_workbench.analysis import multiple_densities, Density

ema_logging.log_to_stderr(ema_logging.INFO)

file_name = './data/500 gas cases no policy.tar.gz'
experiments, outcomes = load_results(file_name)

# pick points in time for which we want to see a
# density subplot
time = outcomes["TIME"][0, :]
times = time[1::math.ceil(time.shape[0] / 5)].tolist()

multiple_densities(experiments, outcomes, log=True, points_in_time=times,
                    density=Density.KDE, fill=False)

plt.show()
