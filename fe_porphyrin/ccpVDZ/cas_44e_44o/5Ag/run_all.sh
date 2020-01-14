#!/bin/bash

DICE_EXE=/projects/jasm3285/apps/Dice/Dice

# Run HF Calculation
# python hf.py

# Run HCISCF Calculation
# python shciscf.py > _shciscf.out

# Run active-active rotations
# python aa.py > _aa.out

# Run final tight Dice calculations
mpirun -np 56 $DICE_EXE final_input_1.dat > final_output.dat
# mpirun -np 56 $DICE_EXE final_input_2.dat >> final_output.dat
# mpirun -np 56 $DICE_EXE final_input_3.dat >> final_output.dat
# mpirun -np 56 $DICE_EXE final_input_4.dat >> final_output.dat

# Perform Extrapolation to FCI Limit
# script requires numpy/scipy
python extrapolate.py > _extrap.out

