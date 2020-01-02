#!/usr/bin/env python
'''
SHCISCF Calculations for pentacene without ptrdm.
'''

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
chkName = '5cene_HF.chk'

mol = lib.chkfile.load_mol( chkName )
mol.max_memory = 40000
mf = scf.RHF( mol )
mf.__dict__.update( lib.chkfile.load( chkName, 'scf') )

# Molecule CASSCF Settings
norb = 22
nelec = 22

# Building SHCISCF Object
mch = shci.SHCISCF( mf, norb, nelec )
mo = mcscf.sort_mo( mch, mf.mo_coeff,[57,59,62,66,67,68,69,70,71,72,73,74,75,76,
					77,78,80,83,92,96,98,100])

mch.chkfile = 'singlet_1Ag_shciscf.chk'
#mo = lib.chkfile.load( mch.chkfile , 'mcscf/mo_coeff')

mch.fcisolver.nPTiter = 0 # No perturbative.
mch.fcisolver.sweep_iter = [ 0, 3, 6, 9 ]
mch.fcisolver.sweep_epsilon = [ 1e-3, 5e-4, 1e-4, 8.5e-5 ]
mch.fcisolver.stochastic = True
mch.fcisolver.mpiprefix = 'mpirun -np 28'
mch.fcisolver.prefix = "/rc_scratch/jasm3285"

# Run SHCISCF
emc = mch.mc2step( mo )[0]
os.system( "rm *.bkp" )

