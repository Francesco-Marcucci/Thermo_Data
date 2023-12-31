from pathlib import Path

import sys

sys.path.append("/home/cfse/Stage_Francesco/Thermodata")

from func.des_turbojet_func import run_turbojet_analysis

from func.des_hbtf_func import run_turbofan_analysis

import pytest

import numpy as np


def test_turbojet():
    alt = 4000  # [ft]
    MN = 0.6
    Fn = 11800  # [lbf]
    new_sol = run_turbojet_analysis(alt, MN, Fn)
    correct_sol = np.array([717.59577021, 818.40663844, 1.57394908]).reshape((3, 1))
    np.testing.assert_almost_equal(new_sol, correct_sol, 5)


def test_turbofan():
    alt = 4000  # [ft]
    MN = 0.6
    Fn = 11800  # [lbf]
    new_sol_tf = run_turbofan_analysis(alt, MN)
    correct_sol_tf = np.array(
        [
            8.11328662e01,
            3.44500820e02,
            1.00000000e00,
            4.19439630e02,
            5.64233274e01,
            1.08865912e-01,
        ]
    ).reshape((6, 1))
    np.testing.assert_almost_equal(new_sol_tf, correct_sol_tf, 5)
