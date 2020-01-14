# Pentacene Calculations

This directory contains PySCF and Dice files to reproduce the data in Table III (Smith 2017).

---
## File Manifest

- singlet_geom: Contains inputs files for calculating energies at the singlet geometry.
- triplet_geom: Contains inputs files for calculating energies at the triplet geometry.
- Each `*_geom` directory contains a 1Ag and 3B2u directory for calcualtions at those symmetries.
- Within each of these is a slurm submit file, a bash script to run all necessary calculation with a single command line command, and all the input files themselves.

```bash
(mpich) jasm3285@login13:pentacene$ find . | sed -e "s/[^-][^\/]*\// |/g" -e "s/|\([^ ]\)/|-\1/"
.
 |-README.md
 |-singlet_geom
 | |-3B2u
 | | |-hf.py
 | | |-run_all.sh
 | | |-submit.sh
 | | |-shciscf.py
 | | |-final_input.dat
 | |-1Ag
 | | |-hf.py
 | | |-slurm.out
 | | |-final_output.dat
 | | |-run_all.sh
 | | |-submit.sh
 | | |-aa.py
 | | |-shciscf.py
 | | |-final_input.dat
 |-triplet_geom
 | |-3B2u
 | | |-hf.py
 | | |-run_all.sh
 | | |-submit.sh
 | | |-shciscf.py
 | | |-final_input.dat
 | |-1Ag
 | | |-hf.py
 | | |-run_all.sh
 | | |-submit.sh
 | | |-final_input.dat
 | | |-shciscf.py
```

---
## Example Usage
To reproduce the data on the first line in Table III:

```bash
cd singlet_geom/1Ag
sh run_all.sh
```

If you run all of the calculations and want to collect the data in an abridged version of 
Table III from Smith 2017. Use the script `collect_data.sh`:

```bash
(mpich) jasm3285@login11:pentacene$ bash collect_data.sh 
      Settings               E_HCISCF             E_SHCI     
      ========               ========             ======     
singlet_geom/1Ag       -841.593616314494      -841.6178705015586
singlet_geom/3B2u      -841.545663883423      -841.5738452503168
triplet_geom/1Ag       -841.582276889202      -841.6093432968245
triplet_geom/3B2u      -841.555559409005      -841.5789973608353
```

---
## Table III Checklist

- [X] singlet_geom/1Ag
  - [X] vHCISCF
  - [X] SHCI
- [ ] singlet_geom/2B2u
  - [X] vHCISCF
  - [X] SHCI
triplet_geom/1Ag  
  - [X] vHCISCF
  - [ ] SHCI
triplet_geom/2B2u  
  - [X] vHCISCF
  - [ ] SHCI