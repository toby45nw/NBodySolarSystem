from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


mpl.rc('font',size=18)
mpl.rc('lines', linewidth=1, marker='', markersize=3, markeredgewidth=3)
mpl.rc('errorbar',capsize=6)
mpl.rc('axes',linewidth=3,grid=False)
mpl.rc('xtick.major',size=10,width=3)
mpl.rc('xtick.minor',visible=False,size=5,width=3)
mpl.rc('ytick.major',size=10,width=3)
mpl.rc('ytick.minor',visible=False,size=5,width=3)

"""

"""


fileNames = ["SunMercuryVenusEarth-dt6500-1578000000-EulerCromer.npy",
"SunMercuryVenusEarth-dt6500-1578000000-Euler.npy",
]

dT = []
TE = []

for file in fileNames:

    Data = np.load(file, allow_pickle=True)     
    print("\nLoading File\n")



    time = []
    PE = []
    KE = []
    x = 0
    y = 0

    for i in range(0, len(Data)):
        time.append(Data[i][0])
        for j in range(1, len(Data[0])):
            x += Data[i][j].potentialEnergy(bodies = Data[i])
            y += Data[i][j].kineticEnergy()

        PE.append(x)
        KE.append(y)
        x = 0
        y = 0

    t1 = np.array(PE)
    t2 = np.array(KE)
    t3 = t1 + t2
    t6 = np.empty(len(t3))

    for i in range(0,len(t3)):
        t6[i] = ((t3[i]-t3[0])/(t3[0]))

    t4 = np.array(time)
    t5 = t4 / (86400*365)

    plt.plot(t5, np.abs(t6), label = "Total Energy")


plt.xlabel("t (years)", fontsize = 20)
plt.ylabel("(E(t)-E(0))/E(0)", fontsize = 20)
plt.title(f"Total Energy against Time")
plt.legend(fontsize = 20, loc = "upper right")
plt.show()
plt.close()