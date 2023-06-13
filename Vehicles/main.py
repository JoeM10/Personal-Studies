import vehicle
import car

print("Camry")
camry = vehicle.automobile("Steering Wheel", 4, 2)
print(type(camry))
print(camry.getSteering())
print(camry.getNumDoors())
camry.setNumWheels(3)
print(camry.getNumWheels())

print("Mustang")
mustang = vehicle.automobile("Steering Wheel", 4, 2)
print(type(mustang))
print(mustang.getSteering())
print(mustang.getNumWheels())
print(mustang.getNumDoors())
