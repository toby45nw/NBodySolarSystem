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
Orbital Period
"""


def quadraticExtreme(x1, y1, x2, y2, x3, y3):
    """Return the value of x that extremises the quadratic y(x) passing through (x1,y1), (x2,y2) and (x3,y3)."""

    a=y1/((x1-x2)*(x1-x3))+y2/((x2-x1)*(x2-x3))+y3/((x3-x1)*(x3-x2))
    b=-y1*(x2+x3)/((x1-x2)*(x1-x3))-y2*(x1+x3)/((x2-x1)*(x2-x3))-y3*(x1+x2)/((x3-x1)*(x3-x2))

    return -b/(2*a) 



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



for i in range(1, len(Data[0])):
    print(f"[{i}] {Data[0][i].name}")

# Prompt the user to enter their choice
while True:
    try:
        choice = int(input("Enter your choice: "))
        # If a valid choice was entered, break out of the loop
        if choice in range(1,len(Data[0])):
            break
        # Otherwise, print an error message
        else:
            print("Please enter a valid choice.")
    except ValueError:
        # If a ValueError is raised (i.e. the input couldn't be converted to an int),
        # print an error message
        print("Please enter a valid choice.")

# Print the chosen option
print(f'You chose: {Data[0][choice].name}')






body = choice
minPoint = -1
maxPoint = -1
# period = 0


# print(Data[0][body].name)

for i in range(1, len(Data) - 1):
    # print(Data[i][body].position[0])
    if Data[i][body].position[0]<=Data[i-1][body].position[0] and Data[i][body].position[0] <= Data[i+1][body].position[0]:
        minPoint=i
    elif Data[i][body].position[0] >= Data[i-1][body].position[0] and Data[i][body].position[0] >= Data[i+1][body].position[0]:
        maxPoint=i

    if minPoint > 0 and maxPoint > 0:
        # A simpler (but less accurate) approximation would be: tl=self.tt[il] ; tr=self.tt[ir].
        # Time when particle is at left turning point.
        tl = quadraticExtreme(Data[minPoint-1][0], Data[minPoint-1][body].position[0], Data[minPoint][0], Data[minPoint][body].position[0],
                                    Data[minPoint+1][0], Data[minPoint+1][body].position[0])
        # Time when particle is at right turning point.
        tr = quadraticExtreme(Data[maxPoint-1][0], Data[maxPoint-1][body].position[0], Data[maxPoint][0], Data[maxPoint][body].position[0],
                                    Data[maxPoint+1][0], Data[maxPoint+1][body].position[0])
        
        period = 2*abs(tr-tl)

print(F"{Data[0][body].name}'s Orbital Period: {(period / (60*60*24)):.1f} days")