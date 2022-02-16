import matplotlib.pyplot as plt

from ema_workbench import ema_logging, load_results
import ema_workbench.analysis.prim as prim

ema_logging.log_to_stderr(level=ema_logging.INFO)

####################################################### H2 18,000 #################################################

def classify(data):
    # get the output for cumulative profit
    ooi = data['Net present value vs time']
    return ooi[:, -1] > 0

# load data
fn = r'./data/12Wind6H2_DoggerBank_AEL_Islandpower_sensitivity4.tar.gz'
results = load_results(fn)

prim_obj = prim.setup_prim(results, classify,
                   #         incl_unc=['Initial well productivity per year','Carbon price multiplier',
                   # 'Initial costs for well development','Operating costs per m3 NG', 'Societal urge to become carbon neutral',
                   # 'Factor onshore to offshore BoP costs', 'Initial wellhead price NG', 'NG learning rate factor'
                   # 'Competition constant offshore hydrogen production', 'Platform modification costs', 'Transitioning factor',
                   # 'Operating cost reduction fraction'],
                            threshold=0.8, threshold_type=1)

box_1 = prim_obj.find_box()
box_1.show_ppt()
box_1.show_tradeoff()
box_1.inspect(20, style='graph', boxlim_formatter="{: .2f}")
box_1.inspect(20)
box_1.select(20)
box_1.write_ppt_to_stdout()
box_1.show_pairs_scatter(20)

# print prim to std_out
print(prim_obj.stats_to_dataframe())
print(prim_obj.boxes_to_dataframe())

# visualize
prim_obj.show_boxes()
plt.show()
