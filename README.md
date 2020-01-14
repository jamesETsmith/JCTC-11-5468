# Reproducing Data From _Cheap and Near Exact CASSCF with Large Active Spaces_
Calculations for the HCISCF Paper (JCTC 2017)

This repository aims to provide an easy and simple way to repoduce the data from Smith 2017 (10.1021/acs.jctc.7b00900).

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