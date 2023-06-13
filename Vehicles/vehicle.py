class automobile(object):
    def __init__(self, steering, numWheels, numDoors):
        self.steering = steering
        self.numWheels = numWheels
        self.numDoors = numDoors

    # Getters
    def getSteering(self):
        return self.steering
    
    def getNumWheels(self):
        return self.numWheels
    
    def getNumDoors(self):
        return self.numDoors
    
    def setNumWheels(self, data):
        self.numWheels = data