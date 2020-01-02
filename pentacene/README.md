# Pentacene Calculations

This directory contains PySCF and Dice files to reproduce the data in Table III (Smith 2017).

## File Manifest

- singlet_geom: Contains inputs files for calculating energies at the singlet geometry.
- triplet_geom: Contains inputs files for calculating energies at the triplet geometry.
- Each `*_geom` directory contains a 1Ag and 3B2u directory for calcualtions at those symmetries.
- Within each of these is a slurm submit file, a bash script to run all necessary calculation with a single command line command, and all the input files themselves.