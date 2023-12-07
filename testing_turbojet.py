from pathlib import Path

from func.des_turbojet_func import run_turbojet_analysis

import numpy as np

if __name__ == "__main__":

    alt = np.linspace(0, 50000, 15)
    # alt = 0

    MN = np.linspace(0, 0.3, 15)

    Fn = np.linspace(900, 20000, 15)

    # run_turbojet_analysis(alt, MN, Fn)

    for x in range(0, 15, 1):

        print(alt[x], MN[x], Fn[x])
        run_turbojet_analysis(alt[x], MN[x], Fn[x])
