# NBodySolarSystem

This project was first started in the University of Lancaster's PHYS281 module.

Libraries Used:
- numpy
- copy
- os
- matplotlib
 

Python Files:
particle.py - particle object that is used by main to create planets and update their motion, Methods are also used by analysis to calculate energy, linear add angular momentum

main.py - Creates instance of planets to be simulated, asking the user for the initial conditions before running the simulation.
Once the simulation is finished the data is saved in a .npy file with a unique name


analysis1.py - Plots Orbits of bodies, asks user to select file

analysis2.py - Plots fractional energy difference, asks user to select file

analysis3.py - Plots fraction angular momentum difference, asks user to select file

analysis4.py - Plots fraction linear momentum  difference, asks user to select file

analysis5.py - calculates the orbital time period, no input

analysis6.py - Subplot of conserved quantities with Euler method using different delta t, no input

analysis7.py - Print out Earths attribute from the last iteration of the simulation, no input

analysis8.py - plots relationship between final fractional energy and delta t with a line of best fit, no input

analysis9.py - subplots of conserved quantities for different numerical methods, no input
