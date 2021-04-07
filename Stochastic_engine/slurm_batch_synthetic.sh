#!/bin/bash

#SBATCH -t 12:00:00
#SBATCH --nodes=12
#SBATCH --ntasks=83
#SBATCH --job-name=synth
#SBATCH -p normal
#SBATCH --export=ALL
#SBATCH --output=out.txt

module load python/3.9.4
source .venv_capow/bin/activate

mpirun python3 -W ignore stochastic_engine.py 50 83 1 
