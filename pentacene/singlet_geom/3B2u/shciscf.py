#!/usr/bin/env python
'''
SHCISCF Calculations for pentacene without ptrdm at the singlet geometry with 3B2u symmetry.
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

# Switch to triplet and set occupation to give overall 3B2u symmetry
mf.mol.spin = 2
mf.irrep_nelec = {'Ag': (18,18), 'B1g': (13,13), 'B2g': (3,3), 'B3g': (3,2), 
	'Au': (2,2), 'B1u': (4,3), 'B2u': (15,15),'B3u': (16,16)}

# Molecule CASSCF Settings
norb = 22
nelec = 22

# Building SHCISCF Object
mch = shci.SHCISCF( mf, norb, nelec )
mo = mcscf.sort_mo( mch, mf.mo_coeff,[57,59,62,66,67,68,69,70,71,72,73,74,75,76,
					77,78,80,83,92,96,98,100])

mch.chkfile = 'singlet_3B2u_shciscf.chk'
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

