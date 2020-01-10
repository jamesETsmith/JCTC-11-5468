# This file reads the appropriate outputs and reconstructs the energies from Table V from Smith 2017.
# 
# Author: James E T Smith <james.smith9113@gmail.com
# Data: 1/10/2020

DIRECTORIES=('ccpVDZ/cas_32e_29o/5Ag' 'ccpVDZ/cas_32e_29o/3B1g' 'ccpVTZ/5Ag' 'ccpVTZ/3B1g')
E_HCISCF=()
E_SHCI=()

# Get HCISCF and SHCI Energies
for d in "${DIRECTORIES[@]}";
do 
    E_HCISCF+=($(grep "CASSCF" $d/_shciscf.out | tail -1 | awk '{print $4}'))
    E_SHCI+=($(tail -1 $d/_extrap.out | awk '{print $3}'))
done

# Print Table V Header
echo "      Settings                   E_HCISCF                E_SHCI     "
echo "      ========                   ========                ======     "

# Print Table V Data
for i in {0..3};
do
    echo ${DIRECTORIES[$i]} "    " ${E_HCISCF[$i]} "    " ${E_SHCI[$i]}
done