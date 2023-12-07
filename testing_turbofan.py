from pathlib import Path

from func.des_hbtf_func_test import run_turbofan_analysis_test

import numpy as np

if __name__ == "__main__":

    alt = np.linspace(0, 50000, 30)
    # alt = 0

    # MN = np.linspace(0, 0.3, 15)
    MN = 0.3

    # Fn = np.linspace(900, 20000, 15)
    Fn = 590
    # run_turbojet_analysis(alt, MN, Fn)

    for x in range(0, 15, 1):

        print(alt[x], MN, Fn)
        run_turbofan_analysis_test(alt[x], MN, Fn)
