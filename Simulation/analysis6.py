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


fileNames = ["SunMercuryVenusEarthMoonMarsJupiterSaturnUranusNeptune-dt3600-378700000-Euler.npy", 
"SunMercuryVenusEarthMoonMarsJupiterSaturnUranusNeptune-dt43200-378700000-Euler.npy",
"SunMercuryVenusEarthMoonMarsJupiterSaturnUranusNeptune-dt86400-378700000-Euler.npy"
]

# create a 1x3 grid of subplots
fig, ax = plt.subplots(3, 1)

for file in fileNames:

    Data = np.load(file, allow_pickle=True)

    

    #Energy Calculation
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

    ax[2].plot(t5, t6)


    #Angular Momentum
    tAM = []
    time = []
    temp = np.array([0,0,0], dtype = float)

    for i in range(0, len(Data)):
        time.append(Data[i][0])
        for j in range(1, len(Data[0])):
            temp += Data[i][j].angularMomentum()

        tAM.append(np.linalg.norm(temp))
        temp = np.array([0,0,0], dtype = float)

    t1 = np.array(time)
    t2 = t1 / (86400*365)

    t3 = np.array(tAM)
    t4 = np.empty(len(t3))

    for i in range(0,len(t4)):
        t4[i] = ((t3[i]-t3[0])/(t3[0]))

    ax[1].plot(t2, t4)
    


    #Linear Momentum
    LM = []
    time = []
    temp = np.array([0,0,0], dtype = float)

    for i in range(0, len(Data)):
        time.append(Data[i][0])
        for j in range(1, len(Data[0])):
            temp += Data[i][j].linearMomentum()
        
        LM.append(np.linalg.norm(temp))
        temp = np.array([0,0,0], dtype = float)

    t1 = np.array(time)
    t2 = t1 / (86400*365)

    t3 = np.array(LM)
    t4 = np.empty(len(t3))

    for i in range(0,len(t4)):
        t4[i] = ((t3[i]-t3[0])/(t3[0]))

    ax[0].plot(t2, t4)






# create a subplot in the first position
ax[0].plot(0,0)

# create a subplot in the second position
ax[1].plot(0,0)

# create a subplot in the third position
ax[2].plot(0,0)


plt.show()