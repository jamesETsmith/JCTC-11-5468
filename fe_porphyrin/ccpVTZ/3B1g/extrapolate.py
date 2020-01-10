import numpy as np
from scipy.stats import linregress


filename = "final_output.dat"

# Tokens to extract energies from Dice output
var_string = "   0    -"
pt_string = "PTEnergy"

# Read file
with open(filename, "r") as f:
    lines = f.readlines()

# Extract energies
var_energies = []
tot_energies = []

for line in lines:
    if var_string in line:
        var_energy = float(line.split()[1])
        var_energies.append(var_energy)
        print("Variational Energy found:", var_energy)

    if pt_string in line and len(line.split()) > 2:
        tot_energy = float(line.split()[1])
        tot_energies.append(tot_energy)
        print("Total Energy found:      ", tot_energy)

# Convert to np.ndarray
var_energies = np.array(var_energies)
tot_energies = np.array(tot_energies)
pt_correction = tot_energies - var_energies

# Linear Regression
slope, intercept, r_value, p_value, std_err = linregress(pt_correction, tot_energies)
print("R value:", r_value)
print("Extrapolated Energy:", intercept)
