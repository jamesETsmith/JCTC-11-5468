# Fe(porphyrin) Calculations

This directory contains input scripts to reproduce the Fe(porphyrin) data from Table V (Smith 2017)

---
## Manifest

```bash
(base) jasm3285@login12:fe_porphyrin$ find . | sed -e "s/[^-][^\/]*\// |/g" -e "s/|\([^ ]\)/|-\1/"
.
 |-README.md
 |-ccpVTZ
 | |-5Ag
 | |-3B1g
 |-ccpVDZ
 | |-cas_44e_44o
 | | |-5Ag
 | | |-3B1g
 | |-cas_32e_29o
 | | |-5Ag
 | | |-3B1g
```

## Example Usage
To reproduce the data on the first line in Table V:

```bash
cd ccpVDZ/cas_32e_29o/5Ag
sh run_all.sh
```

If you run all of the calculations and want to collect the data in an abridged version of 
Table III from Smith 2017. Use the script `collect_data.sh`:

```bash
(mpich) jasm3285@login11:fe_porphyrin$ bash collect_data.sh 
      Settings                   E_HCISCF                E_SHCI     
      ========                   ========                ======     
ccpVDZ/cas_32e_29o/5Ag      -2244.99818876978      -2245.031750189988
ccpVDZ/cas_32e_29o/3B1g     -2244.97104689817      -2245.005277187478
ccpVTZ/5Ag                  -2245.22293263385      -2245.2550990101427
ccpVTZ/3B1g                 -2245.19584329446      -2245.2291244298003
```

## Tabel V Checklist

- [X] ccpVDZ 5Ag CAS (32e, 29o)
  - [X] vHCISCF
  - [X] SHCI
- [X] ccpVDZ 3B1g CAS (32e, 29o)
  - [X] vHCISCF
  - [X] SHCI

- [X] ccpVTZ 5Ag CAS (32e, 29o)
  - [X] vHCISCF
  - [X] SHCI
- [X] ccpVTZ 3B1g CAS (32e, 29o)
  - [X] vHCISCF
  - [X] SHCI

- [ ] ccpVDZ 5Ag CAS (44e, 44o)
  - [ ] vHCISCF
  - [ ] SHCI
- [ ] ccpVDZ 3B1g CAS (44e, 44o)
  - [ ] vHCISCF
  - [ ] SHCI

## Notes
- mc1step() is unstable for AA rotation calculations on 3B1g ccpvdz w/ small basis
