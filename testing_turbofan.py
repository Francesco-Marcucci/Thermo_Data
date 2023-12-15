from pathlib import Path

from func.des_hbtf_func_test import run_turbofan_analysis_test

import numpy as np

# Importing the os module
import os

import shutil

if __name__ == "__main__":

    # alt = np.linspace(150, 30000, 30)
    # alt_1 = alt[::-1].sort()
    # alt_1 = np.array(alt_1)
    # print(alt_1)
    alt = 7000 * 3.2808399

    # MN = np.linspace(0.1, 0.7, 30)
    MN = 0.3

    # Fn = np.linspace(900, 50000, 30)
    Fn = 3000 * 0.22480894387096
    # run_turbojet_analysis(alt, MN, Fn)

    print(alt, MN, Fn)

    run_turbofan_analysis_test(alt, MN, Fn)

    # for x in range(0, 30, 1):

    # print(alt, MN, Fn)
    # run_turbofan_analysis_test(alt, MN, Fn)
    # shutil.rmtree("/home/cfse/Stage_Francesco/Thermo_Data/reports")
