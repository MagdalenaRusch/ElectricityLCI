import os
import pandas as pd

def set_dir(directory):
    if not os.path.exists(directory): os.makedirs(directory)
    return directory


try: modulepath = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/'
except NameError: modulepath = 'electricitylci/'

output_dir = modulepath + 'output/'
data_dir = modulepath + 'data/'


#Declare target year for LCI (recommend current year by default) and year of eGRID data to use
electricity_lci_target_year = 2018
egrid_year = 2016

#emissions data to include in LCI
inventories_of_interest = {'eGRID':'2016','TRI':'2016','NEI':'2016','RCRAInfo':'2015'}
inventories = inventories_of_interest.keys()

#Criteria for filtering eGRID data to include
include_only_egrid_facilities_with_positive_generation = True

egrid_facility_efficiency_filters = {'lower_efficiency':10,
                                     'upper_efficiency':100}

min_plant_percent_generation_from_primary_fuel_category = 90

efficiency_of_distribution_grid = 0.95

model_name = 'ELCI_1'

#Reading the fuel name file
fuel_name = pd.read_csv(data_dir+'fuelname.csv')

#Trading methodology
net_trading = False

#Flow list
fedelemflowlist_version = '0.1'

#Determine whether or not to post-process the generation data
post_process_generation_emission_factors = True

#Set number of standard deviations to use away from the mean to post-process the gen database
post_process_generation_emission_factors_sd_limit = 3

#
def join_with_underscore(items):
    type_cast_to_str = False
    for x in items:
        if not isinstance(x, str):
            # raise TypeError("join_with_underscore()  inputs must be string")
            type_cast_to_str = True
    if type_cast_to_str:
        items = [str(x) for x in items]

    return "_".join(items)

