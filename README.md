# Reproducing Data From _Cheap and Near Exact CASSCF with Large Active Spaces_
Calculations for the HCISCF Paper (JCTC 2017)

This repository aims to provide an easy and simple way to repoduce the data from Smith 2017 ([10.1021/acs.jctc.7b00900](https://pubs.acs.org/doi/abs/10.1021/acs.jctc.7b00900?mi=497hqq0&af=R&AllField=mcscf+casscf&target=default&targetTab=std)).
If you use this work please cite our paper use one of the following:

```
@article{Smith2017,
archivePrefix = {arXiv},
arxivId = {1708.07544},
author = {Smith, James E.T. and Mussard, Bastien and Holmes, Adam A. and Sharma, Sandeep},
doi = {10.1021/acs.jctc.7b00900},
eprint = {1708.07544},
issn = {15499626},
journal = {Journal of Chemical Theory and Computation},
number = {11},
pages = {5468--5478},
title = {{Cheap and Near Exact CASSCF with Large Active Spaces}},
volume = {13},
year = {2017}
}

```

```
James E. T. Smith, Bastien Mussard, Adam A. Holmes, Sandeep Sharma, “Cheap and near exact CASSCF with large active spaces”, J. Chem. Theor. and Comp. 13 (2017) 5468-5478.
```

---
## Hardware Info
- broadwell
- 28 cores, 2.4 GHz
- 128 GB RAM
- 1 TB local disk


---
## Firmware/OS Info
- avx2
- rhel7

---
## Software Info
- Python 3.7.5
- PySCF (git commit: 902d904f8172b6d7c6a75a1bd55257383079cc9f)
  - Compiled with `qcint` library
  - Compiled using mpich2 wrapping gcc 7.3.0
- Dice (git commit: 2ec9beef8d03b2890547189e819491dab505eed5)
  - Compiled using Boost 1.70.0
  - Compiled with mpich wrapping gcc 7.3.0
  - Compiled with Eigen 3.3 (hg commit: 04ab5fa4b241754afcf631117572276444c67239)
  
