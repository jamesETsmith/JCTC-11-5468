from pyscf import lib

# old_file = "/projects/sash2458/Projects/Fe_porphyrin/3B1g/chk_feP_5Ag.chk"
old_file = "/projects/sash2458/Projects/Fe_porphyrin/5Ag/feP_HF.chk"
new_file = "fe_dz_5Ag_hf.chk"
m_old = lib.chkfile.load_mol(old_file)
m_new = lib.chkfile.load_mol(new_file)

mf_old = lib.chkfile.load(old_file, "scf")
mf_new = lib.chkfile.load(new_file, "scf")

print(m_old.atom)
print()
print(m_new.atom)

print(m_old.spin)
print(m_new.spin)
print(m_new.symmetry_subgroup)

print(mf_old["e_tot"])
print(mf_new["e_tot"])
