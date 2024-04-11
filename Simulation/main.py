import numpy as np
from particle import Particle
import copy
import os
import time as ti


Sun = Particle(
    position=np.array([-1.358783303903219E+09, 6.960197478698003E+07, 3.107691085616246E+07]),
    velocity=np.array([7.214199289925677E-01, -1.566954364736395E+01, 1.142648524460107E-01]),
    acceleration=np.array([0, 0,0 ]),
    name = "Sun",
    mass = 1.9896917547517146e+30
)
Mercury = Particle(
    position=np.array([-1.292539766301974E+10, -6.860441274180309E+10, -4.519977545093574E+09]),
    velocity=np.array([3.826456932254077E+04, -5.637271364317362E+03, -3.969059694615271E+03]),
    acceleration=np.array([0, 0, 0]),
    name = "Mercury",
    mass = 3.3031287181409294e+23
)
Venus = Particle(
    position=np.array([-2.831010238780643E+10, -1.051514265274490E+11, 1.416860451501012E+08]),
    velocity=np.array([3.368928007580935E+04, -8.848803089361834E+03, -2.065063845037712E+03]),
    acceleration=np.array([0, 0, 0]),
    name = "Venus",
    mass = 4.870443658170915e+24
)
Earth = Particle(
    position=np.array([7.625112474526837E+10, 1.258661839534181E+11, 2.400206962506473E+07]),
    velocity=np.array([-2.584030337926774E+04, 1.552359568531507E+04, 5.307182811105093E-01]),
    acceleration=np.array([0, 0, 0]),
    name = "Earth",
    mass = 5.976018522278861e+24
)
Moon = Particle(
    position=np.array([7.589397217240274E+010, 1.257368139141052E+11, 3.778365086582303E+07]),
    velocity=np.array([-2.543032933460482E+04, 1.457667093906105E+04, -8.902080984630256E+01]),
    acceleration=np.array([0, 0, 0]),
    name = "Moon",
    mass = 7.350524837+22
)
Mars = Particle(
    position=np.array([8.779135713356672E+10, 2.079320333568181E+11, 2.200680321124747E+09]),
    velocity=np.array([-2.134835678400903E+04, 1.159746158721113E+04, 7.671880889178890E+02]),
    acceleration=np.array([0, 0, 0]),
    name = "Mars",
    mass = 6.42104575922039e+23
)
Jupiter = Particle(
    position=np.array([7.312623037290056E+11, 1.086831508890872E+11, -1.681118417513234E+10]),
    velocity=np.array([-2.069240709375267E+03, 1.353544325088044E+04, -9.868032347522870E+00]),
    acceleration=np.array([0, 0, 0]),
    name = "Jupiter",
    mass = 1.899348304347826e+27
)
Saturn = Particle(
    position=np.array([1.199903575027077E+12, -8.515991086503379E+11, -3.296656763293815E+10]),
    velocity=np.array([5.048981643397958E+03, 7.859379084607269E+03, -3.380060816522228E+02]),
    acceleration=np.array([0, 0, 0]),
    name = "Saturn",
    mass = 5.686837516341829e+26
)
Uranus = Particle(
    position=np.array([2.016541714699770E+12, 2.142934343960371E+12, -1.816572312336063E+10]),
    velocity=np.array([-5.009343330470276E+03, 4.349633436804740E+03, 8.081746349565688E+01]),
    acceleration=np.array([0, 0, 0]),
    name = "Uranus",
    mass = 8.686583592203897e+25
)
Neptune = Particle(
    position=np.array([4.448998109575191E+12, -4.594948469801149E+11, -9.306944283470255E+10]),
    velocity=np.array([5.227209704264918E+02, 5.438593605747424E+03, -1.244416698393460E+02]),
    acceleration=np.array([0, 0, 0]),
    name = "Neptune",
    mass = 1.0247526191904049e+26
)

Halleys = Particle(
    position=np.array([-2.992612598860352E+12, 4.054763051586443E+12, -1.491756536722123E+12]),
    velocity=np.array([6.296409686793425E+02, 6.680200249579649E+02, 6.180479714033787E+01]),
    acceleration=np.array([0, 0, 0]),
    name = "1PHalley's",
    mass = 2.2e+14
)


Star1 = Particle(
    position=np.array([1.496e+11, 0, 0]),
    velocity=np.array([0, 29.8e2, 0]),
    acceleration=np.array([0, 0, 0]),
    name = "Star1",
    mass = 1.989e30
)

Star2 = Particle(
    position=np.array([-1.496e+11, 0, 0]),
    velocity=np.array([0, -29.8e2, 0]),
    acceleration=np.array([0, 0, 0]),
    name = "Star2",
    mass = 1.989e30
)

# self.Bodies = [Sun, Mercury, Venus, Earth, Moon, Mars, Jupiter, Saturn, Uranus, Neptune, Halleys]
# Bodies = [Sun, Mercury, Venus, Earth, Moon, Mars, Jupiter, Saturn, Uranus, Neptune]
Bodies = [Sun, Mercury, Venus, Earth]

# self.Bodies = [Sun, Mercury, Venus, Earth]
# self.Bodies = [Star1, Star2]


def addBodies():
    # Prompt the user to enter their choice
    while True:
        choice = input("Enter your choice: ")
        # If the user's input is a digit, break out of the loop
        if choice.isdigit():
            choice = int(choice)
            # If the choice is in the range 0-9, break out of the loop
            if 0 <= choice <= 9:
                break
            # Otherwise, print an error message
            else:
                print("Please enter a valid choice (a digit from 0 to 9).")
        # If the user's input is not a digit, print an error message
        else:
            print("Please enter a valid choice (a digit from 0 to 9).")

    for i in range(0, choice):
        name1 = str(input("name: "))
        mass1 = float(input("mass: "))
        xPos = float(input("X Position: "))
        yPos = float(input("Y Position: "))
        zPos = float(input("Z Position: "))
        xVel = float(input("X Velocity: "))
        yVel = float(input("Y Velocity: "))
        zVel = float(input("Z Velocity: "))


        tempBody = Particle(
            position=np.array([xPos, yPos, zPos]),
            velocity=np.array([xVel, yVel, zVel]),
            acceleration=np.array([0, 0, 0 ]),
            name = name1,
            mass = mass1
        )

        Bodies.append(tempBody)

    return





# Print the menu
print("""
-----PHYS281 Solar System Simulation-----


What would you like to simulate?
---""")

# Define a dictionary of options
bodyOptions = {
    1: 'Solar System',
    2: 'Add Bodies to Solar System'
}


# Print each option in the dictionary
for key, value in bodyOptions.items():
    print(f'[{key}] {value}')

# Prompt the user to enter their choice
while True:
    try:
        choice = int(input("\nEnter your choice: "))
        # If a valid choice was entered, break out of the loop
        if choice in bodyOptions:
            break
        # Otherwise, print an error message
        else:
            print("Please enter a valid choice.")
    except ValueError:
        # If a ValueError is raised (i.e. the input couldn't be converted to an int),
        # print an error message
        print("Please enter a valid choice.")

# Print the chosen option
print(f'You chose: {bodyOptions[choice]}')
print("\n     -------------------------------     ")


if choice == 2:
    addBodies()




# Define a dictionary of options
methodOptions = {
    1: 'Euler',
    2: 'Euler Cromer',
    3: 'Verlet'
}


# Print the menu
print("\nSimulation Method")
print("----")

# Print each option in the dictionary
for key, value in methodOptions.items():
    print(f'[{key}] {value}')


# Prompt the user to enter their choice
while True:
    try:
        choice = int(input("\nEnter your choice: "))
        # If a valid choice was entered, break out of the loop
        if 1 <= choice <= len(methodOptions):
            break
        # Otherwise, print an error message
        else:
            print("Please enter a valid choice.")
    except ValueError:
        # If a ValueError is raised (i.e. the input couldn't be converted to an int),
        # print an error message
        print("Please enter a valid choice.")

# Print the chosen option
print(f'You chose: {methodOptions[choice]}')
print("\n     -------------------------------     ")



print("\nInitial Conditions")
print("---")

print("***** 3.154e7 seconds in a year *****")

# print(f"""\n------Recommended------

# Iterations = 526600 
# DeltaT = 60

# -----------------------""")
deltaT = int(input("Delta t: "))
tEnd = float(input("Simulation Time: "))

iterations = int(tEnd/deltaT)


# Define dictionary of update methods
updateMethods = {
    1: Particle.eulerUpdate,
    2: Particle.eulerCromerUpdate,
    3: Particle.verletUpdate,
}

# Select update method
try:
    update = updateMethods[choice]
except KeyError:
    raise ValueError("Invalid update method")


tempData = []
Data = []
name = ""
print("\n-----------Simulation Starting-----------")
start = ti.time()

for i in range(0, iterations):
    for j in range(0, len(Bodies)):
        Bodies[j].updateGravitationalAcceleration(Bodies)
    for k in range(0, len(Bodies)):
        update(Bodies[k], deltaT)

    if i == (iterations/10):
        est = (ti.time()- start)

        print(f"\nTime Estimate: {((est*10)/60):.2f} minutes")
        # print(f"Time Estimate: {(est * (10))}")

    if i % 100 == 0:
        time = deltaT * (i+1)
        tempData.append(time)
        for i in range(0,len(Bodies)):
            tempData.append(copy.deepcopy(Bodies[i]))
        Data.append(tempData)
        tempData = []



for i in range(0,len(Bodies)):
    name = name + str(Bodies[i].name)
methods = ["Euler", "EulerCromer", "Verlet"]
fileName = name + "-dt" + str(deltaT) + "-" + str(int(tEnd)) + "-" + methods[choice-1]


np.save(fileName, Data, allow_pickle=True)

print(f"""\nFile Name: {fileName}.npy\n""")
# print(f"Time: {ti.time() - start}s\n")


