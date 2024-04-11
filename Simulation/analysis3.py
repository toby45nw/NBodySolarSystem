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
Angular Momentum
"""


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

plt.plot(t2, t4, label = "Total Angular Momentum")

plt.xlabel("t (years)", fontsize = 20)
plt.ylabel("(L(t)-L(0))/L(0)", fontsize = 20)
plt.title(f"Total Angular Momentum against Time")
plt.legend(fontsize = 20, loc = "upper right")
plt.show()
plt.close()