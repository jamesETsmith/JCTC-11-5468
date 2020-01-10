from pyscf import gto, scf, mcscf, lib
from pyscf.shciscf import shci

# Checkpoint File Name
chkName = "fe_dz_hf.chk"

mol = lib.chkfile.load_mol(chkName)
mol.spin = 4
mol.max_memory = 100000
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
norb = 44
nelec = 44

# Building SHCISCF Object
mch = shci.SHCISCF(mf, norb, nelec)
mo = mcscf.sort_mo_by_irrep(
    mch,
    mf.mo_coeff,
    {"Ag": 6, "B3u": 3, "B2u": 3, "B1g": 4, "B1u": 7, "B2g": 8, "B3g": 8, "Au": 5},
    {"Ag": 21, "B3u": 18, "B2u": 18, "B1g": 12, "B1u": 2, "B2g": 0, "B3g": 0, "Au": 0},
)

mch.chkfile = "fe_dz_5Ag_SHCISCF_44e_44o.chk"
mch.fcisolver.sweep_iter = [0, 3, 6, 9]
mch.fcisolver.sweep_epsilon = [1e-3, 5e-4, 1e-4, 8.0e-5]
mch.fcisolver.stochastic = True
mch.fcisolver.nPTiter = 0  # Turns of PT calculation, i.e. no PTRDM.
mch.fcisolver.mpiprefix = "mpirun -np 28"
mch.fcisolver.prefix = "/rc_scratch/jasm3285/fep/ccpvdz/bigcas/5Ag"
mch.fcisolver.irrep_nelec = {
    "Ag": (4, 3),
    "B3u": (1, 1),
    "B2u": (1, 1),
    "B1g": (3, 2),
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
mch.chkfile = "fe_dz_5Ag_aa_44e_44o.chk"


# Run SHCISCF
mch.mc2step(mo)[0]

