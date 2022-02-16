# from ema_workbench.analysis import feature_scoring
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# from ema_workbench import ema_logging, load_results
#
# ema_logging.log_to_stderr(level=ema_logging.INFO)
#
# # load data
# file_name = r'./data/windhydrogen500.tar.gz'
# experiments, outcomes = load_results(file_name)
#
# x = experiments
# y = outcomes
#
# fs = feature_scoring.get_feature_scores_all(x, y)
# sns.heatmap(fs, cmap='viridis', annot=True)
# plt.show()

################################ OR THE FOLLOWING CODE ##################################
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from ema_workbench import ema_logging, load_results
from ema_workbench.analysis import feature_scoring

ema_logging.log_to_stderr(level=ema_logging.INFO)


# load data
fn = r'./data/offshorecosts.tar.gz'
x, outcomes = load_results(fn)

# we have timeseries so we need scalars
y = {'Costs/MW installed': outcomes['Total costs per MW'][:, -1]
    # 'Hydrogen2grid': np.max(outcomes['Cumulative hydrogen production'], axis=1)
     }


scores = feature_scoring.get_feature_scores_all(x, y)
sns.heatmap(scores, annot=True, cmap='viridis')
plt.show()
