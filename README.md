
## Welcome!

This is a clone of the California and West Coast Power System model ([CAPOW](https://github.com/romulus97/CAPOW_PY36)). This repository is a trimmed down version, isolating the stochastic engine, so that it can be integrated into the California Food-Energy-Water System model ([CALFEWS](https://github.com/hbz5000/CALFEWS)).

First ensure that you have an active Python environment with the modules from the top of each Python script installed. Scripts should be run from the ``Stochastic_engine`` directory. 

The stochastic generator can be run either in serial mode (using a single processor) or parallel mode (using multiple processors). 
- To run in serial mode and create 5 stochastic time series, each 20 water years long, run the command ``python stochastic_engine.py 20 5 0``. 
- To run in parallel mode using 2 processors on a laptop, run the command ``mpirun -n 2 python stochastic_engine.py 20 5 1``. 
- Lastly, for an example of how to run a large experiment on a cluster using the SLURM scheduler, see ``slurm_batch_synthetic.sh``.
