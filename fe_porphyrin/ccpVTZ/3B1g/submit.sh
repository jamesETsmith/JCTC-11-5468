#!/bin/bash
#SBATCH --nodes 2
#SBATCH --output slurm.out
#SBATCH --job-name tz_3B1g_32e
#SBATCH --time=24:00:00
#SBATCH --exclusive
#SBATCH --export=NONE
#SBATCH --qos=blanca-sha

export OMP_NUM_THREADS=28
export I_MPI_FABRICS=shm:tcp
export TMP="/rc_scratch/jasm3285/" #"/scratch/summit/jasm3285"
export TEMP=$TMP
export TMPDIR=$TMP

######################
### Load Conda Env ###
######################
which conda
source activate /projects/jasm3285/conda/envs/mpich
which mpicxx

########################
### Run Calculations ###
########################

sh run_all.sh
rm core.*