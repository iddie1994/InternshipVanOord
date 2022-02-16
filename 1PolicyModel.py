from ema_workbench import (RealParameter, TimeSeriesOutcome, ema_logging,
                           perform_experiments, save_results)
from ema_workbench.em_framework.parameters import Policy
import pysd

model = pysd.read_vensim('/Users/imdij/OneDrive/Bureaublad/THESIS_PYEMA/models/InternshipPilot/SD/Wind_SD.mdl')

model2 = pysd.read_vensim('/Users/imdij/OneDrive/Bureaublad/THESIS_PYEMA/models/InternshipPilot/SD/Wind_SD_nosibsidy.mdl')


from ema_workbench.connectors.pysd_connector import PysdModel

ema_logging.log_to_stderr(ema_logging.INFO)

# Outcomes
outcomes =  [TimeSeriesOutcome('Net present value vs time')
             # TimeSeriesOutcome('Cumulative hydrogen production')
             ]

# Plain Parametric Uncertainties
uncertainties =     [
                    RealParameter('Full load hours',5500,5800),
                    RealParameter('Wake losses',5,9),
                    RealParameter('Curtailment losses',1,3),
                    RealParameter('Inter Array transmission losses',0.7,2),
                    RealParameter('AC collection cable losses',0.7,2),
                    RealParameter('Offshore installation factor', 1.1, 1.3),
                    RealParameter('Island converter terminal power losses',2,4),
                    RealParameter('DC transmission efficiency losses',1.2,3),
                    RealParameter('Port converter terminal power losses',2,3),
                    RealParameter('Cold start up efficiency loss',2,4),
                    RealParameter('Compression efficiency loss',0,1),
                    RealParameter('Water depth hub', 25, 40),
                    RealParameter('H2 system energy requirements loss',2,5),
                    RealParameter('Pipeline efficiency losses', 0, 1),
                    RealParameter('Stack degradation efficiency loss', 1, 2.5),
                    RealParameter('Electrolyser efficiency', 63, 68),
                    RealParameter('Wind hub distance to shore', 130, 150),
                    RealParameter('CAPEX change wind hub', 0.7, 1),
                    RealParameter('CAPEX change electrolysis', 0.7, 1.1),
                    RealParameter('CAPEX change island', 0.7, 1),
                    RealParameter('CAPEX change transport', 0.7, 1),
                    RealParameter('CAPEX change port', 0.7, 1),
                    RealParameter('Electricity price', 55, 60),
                    RealParameter('Hydrogen price', 1.75, 2.75),
                    RealParameter('Subsidy price', 0.5, 1.5),
                    RealParameter('Subsidy period', 8, 20),
                    RealParameter('OPEX wind change', 0.9, 0.91),
                    RealParameter('OPEX electrolysis change', 0.9, 1),
                    RealParameter('Inflation rate', 1, 2),
                    RealParameter('Investment spread', 3, 6),
                    RealParameter('Debt repayment period', 11,14),
                    RealParameter('Debt share', 65, 75),
                    RealParameter('Debt interest', 2, 3),
                    RealParameter('Equity IRR', 10, 12)

                    # RealParameter('Drift parameter', 1.09, 1.11),
                    # RealParameter('Volatility parameter', 0.3, 0.4),
                    # RealParameter('Noise seed', 4, 10)
                     ]

model = PysdModel(mdl_file='/Users/imdij/OneDrive/Bureaublad/THESIS_PYEMA/models/InternshipPilot/SD/Wind_SD.mdl')

model2 = PysdModel(mdl_file='/Users/imdij/OneDrive/Bureaublad/THESIS_PYEMA/models/InternshipPilot/SD/Wind_SD_nosibsidy.mdl')

policies = [Policy('Subsidy',
                   mdl_file='/Users/imdij/OneDrive/Bureaublad/THESIS_PYEMA/models/InternshipPilot/SD/Wind_SD.mdl'),
            Policy('No subsidy',
                   mdl_file='/Users/imdij/OneDrive/Bureaublad/THESIS_PYEMA/models/InternshipPilot/SD/Wind_SD_nosibsidy.mdl')
            ]

model.uncertainties = uncertainties
model.outcomes = outcomes

scenarios= 1000

results = perform_experiments(model, scenarios, policies=policies)

save_results(results, './data/12Wind6H2_DoggerBank_AEL_Island_NoSubsidy.tar.gz')
