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

dT = []
TE = []

for file in fileNames:

    Data = np.load(file, allow_pickle=True)

    x = 0
    y = 0

  

    for i in range(1,len(Data[0])):
        x += Data[-1][i].potentialEnergy(bodies = Data[-1])
        y += Data[-1][i].kineticEnergy()

    TE.append(x+y)
    dT.append(Data[0][0])

coefficients = np.polyfit(dT, TE, 1)
polynomial = np.poly1d(coefficients)
y = polynomial(dT)

plt.plot(dT, y)
plt.plot(dT, TE, "ro")
plt.show()