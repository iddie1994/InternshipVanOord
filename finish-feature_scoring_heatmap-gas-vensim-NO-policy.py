# from ema_workbench.analysis import feature_scoring
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# from ema_workbench import ema_logging, load_results
#
# ema_logging.log_to_stderr(level=ema_logging.INFO)
#
# # load data
# file_name = r'./data/5000 new gas cases no policy.tar.gz'
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
fn = r'./data/10000 gass cases no policy.tar.gz'
x, outcomes = load_results(fn)


# we have timeseries so we need scalars
y = {'Profit': outcomes['Cumulative profit'][:, -1],
    'NG production': np.max(outcomes['NG Production capacity'], axis=1),
    'H2 production': np.max(outcomes['H2 Production capacity'], axis=1)}


scores = feature_scoring.get_feature_scores_all(x, y)
sns.heatmap(scores, annot=True, cmap='viridis')
plt.show()

# from ema_workbench import (RealParameter, TimeSeriesOutcome, ema_logging,
#                            perform_experiments, MultiprocessingEvaluator, save_results)
#
# from ema_workbench.connectors.vensim import VensimModel
#
# if __name__ == "__main__":
#     ema_logging.log_to_stderr(ema_logging.INFO)
#
#     model = VensimModel("InvestmentCase", wd='./models/gas',
#                         model_file='GasInvestmentDynamicsVDSS2.vpmx')
#
#     # outcomes
#     model.outcomes = [TimeSeriesOutcome('Cumulative profit'),
#                       TimeSeriesOutcome('NG Production capacity'),
#                       TimeSeriesOutcome('H2 Production capacity')]
#                       # ,TimeSeriesOutcome('Hydrogen platforms')]
#
#     # Plain Parametric Uncertainties
#     model.uncertainties = [
#         RealParameter('Methane intensity', 0, 120),
#         RealParameter('CO2 emissions per m3 NG produced', 10, 90),
#         RealParameter('Carbon price multiplier', 1, 1.2),
#         RealParameter('CH4 emissions per completed well', 0, 4),
#         RealParameter('CO2 emissions per completed well', 3, 18),
#         RealParameter('Exergy efficiency', 0.6, 1),
#         RealParameter('Initial well productivity per year', 22000000, 30000000),
#         RealParameter('Capacity decay multiplier', 0.145, 0.15),
#         RealParameter('Average well lifetime', 20, 30),
#         RealParameter('Number spot well distribution', 3, 5),
#         RealParameter('NG RD delay', 0.5, 3),
#         RealParameter('Initial costs for well development', 22000000, 27000000),
#         RealParameter('NG learning rate factor', 0.01, 0.1),
#         RealParameter('Property costs per development well', 500000, 2000000),
#         # RealParameter('Success fraction', 0.5, 0.6),#correlates with transitioning factor weird
#         RealParameter('Discovery delay', 2, 5),
#         RealParameter('Initial investable capital', 25000000, 40000000),
#         RealParameter('Operating costs per m3 NG', 0.03, 0.07),
#         RealParameter('Development acceptance fraction', 0.8, 0.95),
#         RealParameter('Construction cost exploration well', 10000000, 15000000),
#         RealParameter('Property desire factor development', 10, 18),
#         RealParameter('Property costs per exploration well', 500000, 1000000),
#         RealParameter('Exploration license delay', 0.75, 2),
#         RealParameter('Property desire factor exploration', 10, 18),
#         RealParameter('Exploration acceptance fraction', 0.8, 0.95),
#
#         RealParameter('Societal urge to become carbon neutral', 0.002, 0.01),
#         RealParameter('Subsidy provision factor', 0.5, 1),
#         RealParameter('Budgeted green investment', 0.02, 0.16),
#         RealParameter('Transport and compression efficiency', 0.005, 0.035),
#         RealParameter('Operating cost reduction fraction', 0.75, 1.25),
#         RealParameter('Effect of weather conditions on stack lifetime', 0.5, 1),
#         RealParameter('Hydrogen system lifetime', 20, 27),
#         RealParameter('Factor onshore to offshore BoP costs', 3, 5),
#         RealParameter('Frequency of new market entrants', 6, 16),
#         RealParameter('Hydrogen construction license delay', 2, 5),
#         RealParameter('Offshore wind acceptance fraction', 0.9, 1),
#         RealParameter('Construction license delay wind', 0.5, 2),
#         RealParameter('Competition constant offshore hydrogen production', 1, 5),
#         RealParameter('Platform distance to shore', 100, 300),
#         RealParameter('Platform modification costs', 3000000, 8000000),
#         RealParameter('Transitioning factor', 1.5, 1.9),
#
#         RealParameter('Price per kg', 1, 6),
#         RealParameter('Volatility parameter', 0.8, 1),
#         RealParameter('Price volatility', 33, 34)]
#
#     nr_experiments = 1000
#     with MultiprocessingEvaluator(model) as evaluator:
#         results = perform_experiments(model, nr_experiments,
#                                       evaluator=evaluator)
#
#     save_results(results, './data/1000 newn gas cases no policy.tar.gz')