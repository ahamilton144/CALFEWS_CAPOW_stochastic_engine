# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:59:48 2018

@author: YSu
"""
from __future__ import division
import time
starttime = time.time()

############################################################################
# HISTORICAL WEATHER AND STREAMFLOW ANALYSIS

# Perform statistical analysis of historical meteorological data
# Note: this script ('calculatte_cov') only needs to be performed once; after
# that stochastic input generation can occur as many times as desired.

# print('Starting covariance calculation')
# import calculate_cov
# print('covariance calculation finished, ', time.time() - starttime)
############################################################################

############################################################################
# STOCHASTIC WEATHER AND STREAMFLOW GENERATION

# Specify a number of synthetic weather years to be simulated. Then
# edit the /cord/data/input/base_inflows.json file, specifying the start and end 
# dates of the forecast_exp scenario flow files. Start date must be 1/1/1901.
# End dates must be 12/31/1901 + stoch_years + 3 after start date. 

stoch_years=20
print('Starting stochastic engine, ', stoch_years, ' years')

# Generate synthetic weather (wind speed and temperature) records. 
import synthetic_temp_wind
synthetic_temp_wind.synthetic(stoch_years)
print('synth weather finished, ', time.time() - starttime)

# Generate synthetic streamflow records 
import synthetic_streamflow
print('streamflows finished, ', time.time() - starttime)

