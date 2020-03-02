import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


filename = "final_output.dat"

# Tokens to extract energies from Dice output
var_string = "   0     -"
pt_string = "PTEnergy"

# Read file
with open(filename, "r") as f:
    lines = f.readlines()

# Extract energies
var_energies = []
tot_energies = []
target_error = None

for line in lines:
    if var_string in line:
        var_energy = float(line.split()[1])
        var_energies.append(var_energy)

    if pt_string in line and len(line.split()) > 2:
        tot_energy = float(line.split()[1])
        tot_energies.append(tot_energy)

    if "targetError" in line and len(line.split()) == 2:
        target_error = float(line.split()[-1])

# Convert to np.ndarray
var_energies = np.array(var_energies)
tot_energies = np.array(tot_energies)
pt_correction = tot_energies - var_energies

# Print and check that energies increase monotonically
header = "Data Extracted from {}".format(filename)
print(header + "\n" + "#" * len(header) + "\n")
print("{:11s}    {:11s}    {:11s}".format("Var.", "Total", "dPT"))
for i in range(var_energies.size):
    if i > 0:
        if var_energies[i - 1] >= var_energies[i]:
            raise AssertionError("Var. energies not increasing!")
        if tot_energies[i - 1] >= tot_energies[i]:
            raise AssertionError("Tot. energies not increasing!")

    print(
        "{:.6f}    {:.6f}    {:.6f}".format(
            var_energies[i], tot_energies[i], pt_correction[i]
        )
    )

# Linear Regression
slope, intercept, r_value, p_value, std_err = linregress(pt_correction, tot_energies)
print("R value:", r_value)
print("Extrapolated Energy:", intercept)

# Estimate error
n_samples = 100
extrap = np.zeros((pt_correction.size * n_samples))

for i, en in enumerate(tot_energies):
    # Generate noise
    noise = np.random.normal(0, target_error, n_samples)

    # Add noise to the total energy
    tot_plus_noise = tot_energies.copy()
    pt_plus_noise = pt_correction.copy()
    for j, d_noise in enumerate(noise):
        tot_plus_noise[i] = en + d_noise
        pt_plus_noise[i] = pt_correction[i] + d_noise
        extrap[i * n_samples + j] = linregress(pt_plus_noise, tot_plus_noise)[1]

# Print Data
header = "Extrap. Energy Error Analysis (includes noise)"
print("\n" + header + "\n" + "#" * len(header) + "\n")
print("Energy spread [{:.6f} - {:.6f}] (Ha)".format(extrap.min(), extrap.max()))
print(
    "Mean Extrap. Energy = {:.6f} +\- {:.2e} (Ha)".format(
        np.mean(extrap), np.std(extrap)
    )
)


# Plot Extrapolation
plt.figure()
x = np.linspace(pt_correction.min() * 1.1, 0)
y = x * slope + intercept
plt.plot(x, y, c="r")
plt.scatter(pt_correction, tot_energies)

plt.xlabel("PT Correction (Ha)")
plt.ylabel("Total Energy (Ha)")
plt.tight_layout()
plt.savefig("extrap.png", dpi=600)

