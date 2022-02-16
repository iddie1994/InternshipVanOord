import matplotlib.pyplot as plt
import seaborn as sns

from ema_workbench import load_results
from ema_workbench.analysis import clusterer, plotting, Density

# load data
fn = r'./data/500 gas cases no policy.tar.gz'
experiments, outcomes = load_results(fn)
data = outcomes['Cumulative profit']

# calcuate distances
distances = clusterer.calculate_cid(data)

# plot dedrog
# clusterer.plot_dendrogram(distances)

# do agglomerative clustering on the distances
clusters = clusterer.apply_agglomerative_clustering(distances,
                                                    n_clusters=5)

# show the clusters in the output space
x = experiments.copy()
x['clusters'] = clusters.astype('object')
plotting.lines(x, outcomes,  group_by='clusters',
               density=Density.VIOLIN)

# show the input space
# sns.pairplot(x, hue='clusters',
#              vars=['Initial well productivity per year','Carbon price multiplier',
#                    'Initial costs for well development','Operating costs per m3 NG', 'Societal urge to become carbon neutral',
#                    'Subsidy provision factor', 'Factor onshore to offshore BoP costs',
#                    'Competition constant offshore hydrogen production', 'Platform modification costs', 'Transitioning factor',
#                    'Price volatility'],
#              plot_kws=dict(s=13))
plt.show()