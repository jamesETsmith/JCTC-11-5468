#!/usr/bin/env python
"""
SHCISCF Calculations for pentacene without ptrdm with symmetry of 3B2u at the triplet optimized geometry.
"""

from pyscf import gto
from pyscf import scf
from pyscf import mcscf
from pyscf import dmrgscf
from pyscf import tools
from pyscf import ao2mo
from pyscf import symm
from pyscf.shciscf import shci
from pyscf import lib
import numpy
from pyscf.tools.dump_mat import dump_mo
from pyscf.tools import molden
import scipy.linalg
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
# fmt: off
mo = mcscf.sort_mo( mch, mf.mo_coeff,[57, 58, 62, 66, 67, 68, 69, 70, 71, 72,
	 73, 74, 75, 76, 77, 78, 79, 81, 92, 96, 98, 100])
# fmt: on

mch.chkfile = "triplet_1Ag_shciscf.chk"
# mo = lib.chkfile.load( mch.chkfile , 'mcscf/mo_coeff')

mch.fcisolver.nPTiter = 0  # No perturbative.
mch.fcisolver.sweep_iter = [0, 3, 6, 9]
mch.fcisolver.sweep_epsilon = [1e-3, 5e-4, 1e-4, 8.5e-5]
mch.fcisolver.stochastic = True
mch.fcisolver.mpiprefix = "mpirun -np 28"
mch.fcisolver.prefix = "/rc_scratch/jasm3285/t3B2u"

# Run SHCISCF
emc = mch.mc2step(mo)[0]
os.system("rm *.bkp")
