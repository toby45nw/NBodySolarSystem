import numpy as np

class Particle:
    """

    """

    def __init__(
        self,
        position=np.array([0, 0, 0], dtype=float),
        velocity=np.array([0, 0, 0], dtype=float),
        acceleration=np.array([0, 0, 0], dtype=float),
        name='Ball',
        mass=1.0,
        G = 6.67408E-11
        ):
        self.position = np.copy(position).astype(float)
        self.velocity = np.copy(velocity).astype(float)
        self.acceleration = np.copy(acceleration).astype(float)
        self.name = name
        self.mass = mass
        self.G = G
        self.prevAcceleration = np.array([0, 0, 0], dtype = float)

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass,self.position, self.velocity, self.acceleration)

    def getPosition(self):
        return self.position

    def updateGravitationalAcceleration(self, bodies):
        self.bodies = bodies
        self.prevAcceleration = self.acceleration
        self.acceleration = np.array([0, 0, 0], dtype = float)
        for i in range(0, len(bodies)):
            if bodies[i].name != self.name:
                posVec = np.array([0, 0, 0], dtype=float)
                posVec = self.position - bodies[i].position
                x = (np.linalg.norm(posVec))
                self.acceleration += (-1 * (self.G * bodies[i].mass)/(x ** 2)) * (posVec / x)


    def eulerUpdate(self, deltaT):
        self.position = self.position + (self.velocity * deltaT)
        self.velocity = self.velocity + (self.acceleration * deltaT)
        
    def eulerCromerUpdate(self, deltaT):
        self.velocity = self.velocity + (self.acceleration * deltaT)
        self.position = self.position + (self.velocity * deltaT)

    def verletUpdate(self, deltaT):
        self.position = self.position + (self.velocity * deltaT) + ((1/2) * self.prevAcceleration*deltaT ** 2)
        self.velocity = self.velocity + ((1/2) * (self.prevAcceleration + self.acceleration) * deltaT)   
    
    def kineticEnergy(self):
        kineticEnergy = (1/2) * self.mass * (np.linalg.norm(self.velocity) ** 2)
        return kineticEnergy

    def potentialEnergy(self, bodies):
        # Initialize potential energy to 0
        U = 0

        # print(self.name)
        # Loop over all particles
        for i in range(1, len(bodies)):

            # Check if the particle is not the same as the current particle
            if bodies[i].name != self.name:
                # Calculate distance between the current particle and the other particle
                r = np.linalg.norm(self.position - bodies[i].position)
                # Add the gravitational potential energy to the total potential energy
                U += -1 * ((self.G * self.mass * bodies[i].mass) / r)

                
                # print(U)

        # Return the total potential energy
        return U

    def linearMomentum(self):
        # Calculate linear momentum as the product of mass and velocity
        p = self.mass * self.velocity
        # Return linear momentum as a vector
        return p

    #Need to adjust to the barry center coordinates
    def angularMomentum(self):
        # Calculate cross product of position vector and velocity vector
        L = np.cross(self.position, (self.mass * self.velocity))
        # Return angular momentum as a vector
        return L
