import numpy as np

from ema_workbench import (RealParameter, TimeSeriesOutcome, ema_logging,
                           ScalarOutcome, perform_experiments, save_results)
from ema_workbench.em_framework.parameters import Policy
from ema_workbench.connectors.vensim import VensimModel

if __name__ == '__main__':
    ema_logging.log_to_stderr(ema_logging.INFO)

    model = VensimModel("InvestmentCase", wd='./models/hydrogenprice',
                        model_file='HydrogenPrice1.vpmx')#5

    # outcomes
    model.outcomes =  [TimeSeriesOutcome('Cumulative profit'),
                      # TimeSeriesOutcome('Cumulative investments in hydrogen R&D'),
                      # TimeSeriesOutcome('NG Production capacity'),
                       TimeSeriesOutcome('H2 Production capacity')]

    # Plain Parametric Uncertainties
    model.uncertainties = [
        RealParameter('Methane intensity', 0, 120),
        RealParameter('CO2 emissions per m3 NG produced', 10, 90),
        RealParameter('Carbon price multiplier', 1, 1.3),
        RealParameter('CH4 emissions per completed well', 0, 4),
        RealParameter('CO2 emissions per completed well', 3, 18),
        RealParameter('Exergy efficiency', 0.6, 1),
        RealParameter('Initial well productivity per year', 21000000, 30000000),
        RealParameter('Capacity decay multiplier', 0.145, 0.16),
        RealParameter('Average well lifetime', 20, 30),
        RealParameter('Number spot well distribution', 3, 5),
        RealParameter('NG RD delay', 0.5, 3),
        RealParameter('Initial costs for well development', 22000000, 27000000),
        RealParameter('NG learning rate factor', 0.01, 0.1),
        RealParameter('Property costs per development well', 500000, 2000000),
        RealParameter('Success fraction', 0.5, 0.6),#correlates with transitioning factor weird
        RealParameter('Discovery delay', 2, 5),
        RealParameter('Initial investable capital', 25000000, 40000000),
        RealParameter('Operating costs per m3 NG', 0.03, 0.08),
        RealParameter('Development acceptance fraction', 0.8, 0.95),
        RealParameter('Construction cost exploration well', 10000000, 15000000),
        RealParameter('Property desire factor development', 10, 18),
        RealParameter('Property costs per exploration well', 500000, 1000000),
        RealParameter('Exploration license delay', 0.75, 2),
        RealParameter('Property desire factor exploration', 10, 18),#
        RealParameter('Exploration acceptance fraction', 0.8, 0.95),
        RealParameter('Initial wellhead price NG', 0.22, 0.25),

        # RealParameter('Frequency of new market entrants', 6, 16),
        # RealParameter('Societal urge to become carbon neutral', 0.0001, 0.01),
        # RealParameter('Subsidy provision factor', 0.3, 1),
        # RealParameter('Budgeted green investment', 0.02, 0.1),
        RealParameter('Transport and compression efficiency', 0.005, 0.035),
        RealParameter('Operating cost reduction fraction', 1, 1.2), ###
        RealParameter('Effect of weather conditions on stack lifetime', 0.5, 1),
        RealParameter('Hydrogen system lifetime', 20, 27),
        RealParameter('Factor onshore to offshore BoP costs', 3, 5),
        RealParameter('Hydrogen construction license delay', 2, 5),
        RealParameter('Offshore wind acceptance fraction', 0.9, 1),#
        RealParameter('Construction license delay wind', 0.5, 2),
        RealParameter('Competition constant offshore hydrogen production', 1, 5),
        RealParameter('Platform distance to shore', 100, 300),
        RealParameter('Platform modification costs', 2000000, 8000000),
        RealParameter('Transitioning factor', 1.3, 1.9),
        # RealParameter('Infrastructure availability', 0.95, 1),#
        # RealParameter('Price per kg', 1, 6),
        RealParameter('Volatility parameter', 0.8, 1),
        RealParameter('Price volatility', 33, 34)]

    # add policies
    policies = [Policy('100% green in 2050 without governmental support',
                       model_file=r'HydrogenPrice3c.vpmx'),
                Policy('100% green in 2050 with governmental support',
                       model_file=r'HydrogenPrice3d.vpmx'),
                Policy('No green urge and budgeting',
                model_file = r'HydrogenPrice3a.vpmx'),
                # Policy('No green urge and budgeting with governmental support',
                # model_file=r'HydrogenPrice3b.vpmx')
                # Policy('2 euro/kg H2',
                #        model_file=r'HydrogenPrice2.vpmx'),
                # Policy('3 euro/kg H2',
                #        model_file=r'HydrogenPrice3.vpmx'),
                # Policy('4 euro/kg H2',
                #        model_file=r'HydrogenPrice4.vpmx'),
                # Policy('5 euro/kg H2',
                #        model_file=r'HydrogenPrice5.vpmx'),)
                ]

    results = perform_experiments(model, 2000, policies=policies)

    save_results(results, './data/policy3 h2 sensitivity.tar.gz')