from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os

mpl.rc('font',size=18)
mpl.rc('lines', linewidth=1, marker='', markersize=3, markeredgewidth=3)
mpl.rc('errorbar',capsize=6)
mpl.rc('axes',linewidth=3,grid=False)
mpl.rc('xtick.major',size=10,width=3)
mpl.rc('xtick.minor',visible=False,size=5,width=3)
mpl.rc('ytick.major',size=10,width=3)
mpl.rc('ytick.minor',visible=False,size=5,width=3)


"""
Orbit Plot
"""

AU = 1.495978707e11


options = []
print("\nFile Select")
print("----")

for line in os.listdir():
    if ".npy" in line:
        options.append(line)

# Print each option in the list with a number
for i, option in enumerate(options):
    print(f'[{i+1}]\t{option}')
        
# Prompt the user to enter their choice
while True:
    try:
        choice = int(input("Enter your choice: "))
        # If a valid choice was entered, break out of the loop
        if 1 <= choice <= len(options):
            break
        # Otherwise, print an error message
        else:
            print("Please enter a valid choice.")
    except ValueError:
        # If a ValueError is raised (i.e. the input couldn't be converted to an int),
        # print an error message
        print("Please enter a valid choice.")

fileName = options[choice - 1]

print(f"Loading {fileName}")

Data = np.load(fileName, allow_pickle=True)     
print("\nLoading File\n")



numBodies = len(Data[0])
xPos = []
yPos = []

for i in range(1, numBodies):
    for j in range(0, len(Data)):
        xPos.append(Data[j][i].position[0])
        yPos.append(Data[j][i].position[1])

        xpos = np.array(xPos)
        ypos = np.array(yPos)

        xpos = xpos/AU
        ypos = ypos/AU

    plt.plot(xpos, ypos, label = str(Data[0][i].name))
    xPos = []
    yPos = []

plt.text(0.01, 0.01, f"Simulation Time: {(Data[-1][0] / (86400*365)):.2f} Years", horizontalalignment='left', verticalalignment='bottom', transform=plt.gca().transAxes)
    
plt.xlabel("X (AU)", fontsize = 20)
plt.ylabel("Y (AU)", fontsize = 20)
plt.title(f"Solar System Orbits")
plt.legend(fontsize=20, loc = "upper right")
plt.show()
plt.close()