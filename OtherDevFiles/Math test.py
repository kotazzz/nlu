from NewLifeUtils import *
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    time_main_start = datetime.datetime.now()  ########################
    tbm = TableBuildModule()
    cm = ColorModule()
    sm = StringUtilModule()
    now = datetime.datetime.now()
    data = []
    gr_nval = []
    gr_elapsed = []
    gr_rslen = []
    maxc = 2000
    rawSeed = 1
    formula = (now.microsecond ** 3) * (now.second ** 10) + (now.month * now.day)
    for n in range(0, maxc, 1):
        time_calc_start = datetime.datetime.now()  ########################
        rawSeed = formula ** n
        time_calc_end = datetime.datetime.now()  ########################
        data.append(
            f"{n};{sm.screate((time_calc_end-time_calc_start).total_seconds(),8)};{len(str(rawSeed))}"
        )
        gr_nval.append(n)
        gr_elapsed.append((time_calc_end - time_calc_start).total_seconds())
        gr_rslen.append(len(str(rawSeed)))
        if n % 100 == 0:
            print(f"{cm.ACC.CLEARSCREEN} Calcuclation {n}/{maxc}")
    fig = plt.figure()
    nval_elapsed = fig.add_subplot(211)
    nval_rslen = fig.add_subplot(212)
    nval_elapsed.plot(gr_nval, gr_elapsed)
    nval_rslen.plot(gr_nval, gr_rslen)
    plt.show()
    table = tbm.createTable(5, [22, 22, 22, 22, 22], data, header=False)
    i = 1
    while os.path.exists(f'test-{now.strftime("%d-%m-%Y")}-{i}.txt'):
        i += 1
    f = open(f'test-{now.strftime("%d-%m-%Y")}-{i}.txt', "w", encoding="utf8")
    f.write(sm.remove_csi(table))
    f.close()
    print(cm.ACC.CLEARSCREEN + table)
    time_main_end = datetime.datetime.now()  ########################
    print("--- %s ---" % (time_main_end - time_main_start))  #######################
