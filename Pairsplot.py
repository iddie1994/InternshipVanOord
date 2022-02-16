
import numpy as np
import matplotlib.pyplot as plt

from ema_workbench import load_results, ema_logging

from ema_workbench.analysis.pairs_plotting import (pairs_lines, pairs_scatter,
                                                   pairs_density)

ema_logging.log_to_stderr(level=ema_logging.DEFAULT_LEVEL)

# load data
fn = r'./data/windhydrogen100.tar.gz'
experiments, outcomes = load_results(fn)

# transform the results to the required format
# that is, we want to know the max peak and the casualties at the end of the
# run
tr = {}

for key, value in outcomes.items():
    if key == 'Cumulative hydrogen production':
        tr[key] = value[:, -1]  # we want the end value
    else:
        # we want the maximum value of the peak
        max_peak = np.max(value, axis=1)
        tr['max peak'] = max_peak

        # we want the time at which the maximum occurred
        # the code here is a bit obscure, I don't know why the transpose
        # of value is needed. This however does produce the appropriate results
        logical = value.T == np.max(value, axis=1)

pairs_scatter(experiments, tr, filter_scalar=False)
pairs_lines(experiments, outcomes)
pairs_density(experiments, tr, filter_scalar=False)
plt.show()
