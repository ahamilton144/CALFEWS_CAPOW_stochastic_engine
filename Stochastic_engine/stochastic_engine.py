# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:59:48 2018

@author: YSu
"""
from __future__ import division
import time
import sys
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

stoch_years = int(sys.argv[1])
nsamples = int(sys.argv[2])
parallel_mode = int(sys.argv[3])

if parallel_mode == 1:
  from mpi4py import MPI
  import math
  import time
  # Parallel simulation
  comm = MPI.COMM_WORLD
  # Number of processors and the rank of processors
  rank = comm.Get_rank()
  nprocs = comm.Get_size()
  # Determine the chunk which each processor will neeed to do
  count = int(math.floor(nsamples/nprocs))
  remainder = nsamples % nprocs
  # Use the processor rank to determine the chunk of work each processor will do
  if rank < remainder:
    start = rank*(count+1)
    stop = start + count + 1 
  else:
    start = remainder*(count+1) + (rank-remainder)*count 
    stop = start + count 
  print(nprocs, rank, count, remainder, start, stop)
else:
  start = 0
  stop = nsamples

for s in range(start, stop):
  s = str(s)
  print('Starting stochastic engine, sample ', s, ', ', stoch_years, ' years')

  # Generate synthetic weather (wind speed and temperature) records. 
  import synthetic_temp_wind
  synthetic_temp_wind.synthetic(stoch_years - 2, s)
  print('synth weather finished, ', time.time() - starttime)

  # Generate synthetic streamflow records 
  import synthetic_streamflow
  synthetic_streamflow.run(s)
  print('streamflows finished, ', time.time() - starttime)

