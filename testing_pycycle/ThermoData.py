from pathlib import Path

from func.des_hbtf_func import run_turbofan_analysis

from func.des_turbojet_func import run_turbojet_analysis

from func.des_hbtf_func_test import run_turbofan_analysis_test


if __name__ == "__main__":

    alt = float(input("insert altitude [ft]: "))

    MN = float(input("insert mach number[adim]: "))

    Fn = float(input("insert net force[lbf]: "))

    a = float(input("press 1 to perform turbojet 2 to perform turbofan: "))

    if a == 1:
        run_turbojet_analysis(alt, MN, Fn)

    if a == 2:
        run_turbofan_analysis_test(alt, MN)


# / 0.3048
# * 0.22480894387096
