#!/usr/bin/env python
"""
SHCISCF Calculations for pentacene without ptrdm. Using active-active rotations to improve active space orbitals.
"""

from pyscf import gto
from pyscf import scf
from pyscf import mcscf
from pyscf import symm
from pyscf.shciscf import shci
from pyscf import lib
import numpy
import os

# Checkpoint File Name
chkName = "5cene_HF_triplet.chk"

mol = lib.chkfile.load_mol(chkName)
mol.max_memory = 40000
mf = scf.RHF(mol)
mf.__dict__.update(lib.chkfile.load(chkName, "scf"))

# Ensure we're dealing with triplet
mf.irrep_nelec = {
    "Ag": (18, 18),
    "B1g": (13, 13),
    "B2g": (3, 3),
    "B3g": (3, 2),
    "Au": (2, 2),
    "B1u": (4, 3),
    "B2u": (15, 15),
    "B3u": (16, 16),
}

# Molecule CASSCF Settings
norb = 22
nelec = 22

# Building SHCISCF Object
mch = shci.SHCISCF(mf, norb, nelec)

# Load previous SHCISCF calc.
mch.chkfile = "triplet_3B2u_shciscf.chk"
mo = lib.chkfile.load(mch.chkfile, "mcscf/mo_coeff")

# Set SHCI settings
mch.fcisolver.nPTiter = 0  # No perturbative.
mch.fcisolver.sweep_iter = [0, 3, 6, 9]
mch.fcisolver.sweep_epsilon = [1e-3, 5e-4, 1e-4, 8.5e-5]
mch.fcisolver.stochastic = True
mch.fcisolver.mpiprefix = "mpirun -np 28"
mch.fcisolver.scratchDirectory = "/rc_scratch/jasm3285/5cene/triplet/3B2u"

# AA Rotations
mch.chkfile = "triplet_3B2u_aa.chk"
mch.internal_rotation = True
mch.frozen = list(range(mch.ncore)) + list(range(mch.ncore + mch.ncas, mo.shape[1]))
mch.max_cycle_macro = 10

# Run SHCISCF
emc = mch.mc2step(mo)[0]
os.system("rm *.bkp")

