import vehicle
import car

print("Camry")
camry = vehicle.automobile("Steering Wheel", 4, 2)
print(type(camry))
print("Camry Steering: " + str(camry.getSteering()))
camry.setNumWheels(3)
print("Camry Wheels: " + str(camry.getNumWheels()))
print("Camry Doors: " + str(camry.getNumDoors()))

print("Mustang")
mustang = vehicle.automobile("Steering Wheel", 4, 2)
print(type(mustang))
print("Mustang Steering: " + str(mustang.getSteering()))
print("Mustang Wheels: " + str(mustang.getNumWheels()))
print("Mustang Doors: " + str(mustang.getNumDoors()))
