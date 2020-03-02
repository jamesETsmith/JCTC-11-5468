#!/bin/bash
######################################################################
#                                                                    #
# Set the arguments up and here and the script will take care of any # 
# differences between summit and blanca.                             #
#                                                                    #
# Author: James E. T. Smith <james.smith9113@gmail.com>              #
# Date: 1/28/2020                                                    #
#                                                                    #
# Sample usage:                                                      #
#   $ ./submit.sh                                                    #
#                                                                    #
######################################################################

#################
# User settings #
#################

USER_NODES=1
USER_TIME="24:00:00"
USER_CONDA_ENV=mpich
USER_JOB_NAME="FeP_3B1g"
USER_OMP_NUM_THREADS=48
USER_VERBOSE=true
USER_OUTPUT="slurm.out"
USER_PARTITION="smem"


#######################################
# Check to see which cluster we're on #
#######################################
ON_SUMMIT=false
QUEUE_ACC="--qos=blanca-sha"
USER_TMP=/rc_scratch/jasm3285/
if env | grep -q "summit/etc/slurm.conf"
then
    echo "ON SUMMIT"
    ON_SUMMIT=true
    QUEUE_ACC="-A ucb-summit-sha"
    USER_TMP=/scratch/summit/jasm3285
else
    echo "ON BLANCA"
    USER_PARTITION="blanca-sha"
fi

######################
# Print user options #
######################
if ${USER_VERBOSE}
then
    echo "General Settings"
    echo "================"
    echo "Activating Conda Env = ${USER_CONDA_ENV}"
    echo "Wall time limit = ${USER_TIME}"
    echo "Job Name = ${USER_JOB_NAME}"
    echo "Queue/Account Info = ${QUEUE_ACC}"
    echo "Partition = ${USER_PARTITION}"
    echo "Using tmp directory = ${USER_TMP}"
    echo "Number of node(s) = ${USER_NODES}"
    echo "Setting OMP_NUM_THREADS = ${USER_OMP_NUM_THREADS}"
    echo "Slurm output file = ${USER_OUTPUT}"
    echo ""
fi


############################################
# Here is the constructed slurm batch file #
############################################

# sbatch << EOF
echo "#!/bin/bash
#SBATCH --nodes ${USER_NODES}
#SBATCH --output ${USER_OUTPUT}
#SBATCH --job-name ${USER_JOB_NAME}
#SBATCH --time=${USER_TIME}
#SBATCH --exclusive
#SBATCH --export=NONE
#SBATCH ${QUEUE_ACC}
#SBATCH --partition=${USER_PARTITION}

export OMP_NUM_THREADS=${USER_OMP_NUM_THREADS}
export I_MPI_FABRICS=shm:tcp
export TMP=${USER_TMP}
export TEMP=${USER_TMP}
export TMPDIR=${USER_TMP}
​
######################
### Load Conda Env ###
######################
which conda
source activate /projects/jasm3285/conda/envs/${USER_CONDA_ENV}

########################
### Run Calculations ###
########################

sh run_all.sh
​
" > _slurm_batch.sh

sbatch _slurm_batch.sh

rm _slurm_batch.sh # Comment out to see record of slurm job
