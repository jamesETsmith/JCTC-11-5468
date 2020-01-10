from pyscf import gto, scf, mcscf, lib
from pyscf.shciscf import shci

# Checkpoint File Name
chkName = "fe_tz_hf.chk"

mol = lib.chkfile.load_mol(chkName)
mol.spin = 4
mf = scf.RHF(mol)
mf.__dict__.update(lib.chkfile.load(chkName, "scf"))
mf.irrep_nelec = {
    "Ag": (25, 24),
    "B3u": (19, 19),
    "B2u": (19, 19),
    "B1g": (15, 14),
    "B1u": (7, 7),
    "B2g": (4, 3),
    "B3g": (4, 3),
    "Au": (2, 2),
}


# Molecule CASSCF Settings
norb = 29
nelec = 32

# Building SHCISCF Object
mch = shci.SHCISCF(mf, norb, nelec)
mo = mcscf.sort_mo_by_irrep(
    mch,
    mf.mo_coeff,
    {"Ag": 2, "B3u": 0, "B2u": 0, "B1g": 1, "B1u": 7, "B2g": 7, "B3g": 7, "Au": 5},
    {"Ag": 23, "B3u": 19, "B2u": 19, "B1g": 14, "B1u": 2, "B2g": 0, "B3g": 0, "Au": 0},
)

mch.chkfile = "fe_tz_5Ag_SHCISCF.chk"
mch.fcisolver.sweep_iter = [0, 3, 6]
mch.fcisolver.sweep_epsilon = [1e-3, 5e-4, 1e-4]
mch.fcisolver.stochastic = True
mch.fcisolver.nPTiter = 0  # Turns of PT calculation, i.e. no PTRDM.
mch.fcisolver.mpiprefix = "mpirun -np 28"
mch.fcisolver.prefix = "/rc_scratch/jasm3285/fep/ccpvdz/smallcas/5Ag"
mch.fcisolver.irrep_nelec = {
    "Ag": (2, 1),
    "B3u": (0, 0),
    "B2u": (0, 0),
    "B1g": (1, 0),
    "B1u": (5, 5),
    "B2g": (4, 3),
    "B3g": (4, 3),
    "Au": (2, 2),
}

# Active-active rotations
mo = lib.chkfile.load(mch.chkfile, "mcscf/mo_coeff")
mch.frozen = list(range(mch.ncore)) + list(range(mch.ncore + mch.ncas, mo.shape[1]))
mch.internal_rotation = True
mch.max_cycle_macro = 15
mch.chkfile = "fe_tz_5Ag_aa.chk"


# Run SHCISCF
mch.mc2step(mo)[0]

