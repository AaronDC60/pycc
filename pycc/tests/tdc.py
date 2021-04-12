"""
Test CCSD equation solution using various molecule test cases.
"""

# Import package, test suite, and other packages as needed
import psi4
import pycc
import pytest
import sys
sys.path.insert(0, '../data')
import molecules as mol

# Psi4 Setup
psi4.set_memory('2 GiB')
psi4.core.set_output_file('output.dat', False)
memory = 2
psi4.set_options({'basis': 'STO-3G',
                  'scf_type': 'pk',
                  'mp2_type': 'conv',
                  'freeze_core': 'true',
                  'e_convergence': 1e-12,
                  'd_convergence': 1e-12,
                  'r_convergence': 1e-12,
                  'diis': 1})
mol = psi4.geometry(mol.moldict["H2O"])
rhf_e, rhf_wfn = psi4.energy('SCF', return_wfn=True)

maxiter = 75
e_conv = 1e-12
r_conv = 1e-12
ccsd = pycc.ccenergy(rhf_wfn, memory)
eccsd = ccsd.solve_ccsd(e_conv,r_conv,maxiter)