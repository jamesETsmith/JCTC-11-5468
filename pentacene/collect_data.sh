# This file reads the appropriate outputs and reconstructs the energies from Table III from Smith 2017.
# 
# Author: James E T Smith <james.smith9113@gmail.com
# Data: 1/10/2020

DIRECTORIES=('singlet_geom/1Ag' 'singlet_geom/3B2u' 'triplet_geom/1Ag' 'triplet_geom/3B2u')
E_HCISCF=()
E_SHCI=()

# Get HCISCF and SHCI Energies
for d in "${DIRECTORIES[@]}";
do 
    E_HCISCF+=($(grep "CASSCF" $d/_shciscf.out | tail -1 | awk '{print $4}'))
    E_SHCI+=($(tail -1 $d/_extrap.out | awk '{print $5}'))
done

# Print Table V Header
echo "      Settings               E_HCISCF             E_SHCI     "
echo "      ========               ========             ======     "

# Print Table V Data
for i in {0..3};
do
    echo ${DIRECTORIES[$i]} "    " ${E_HCISCF[$i]} "    " ${E_SHCI[$i]}
done