#authors' name is Julia Schutz
class Ambulance:
    """describes an ambulance"""
myAmbulance = Ambulance()

myAmbulance.speed = 60
myAmbulance.priority = 1
myAmbulance.capacity = 2

import math

def ambulance1(m):
    controlled_velocity = -10*(1-m.priority) + 2.37*(m.speed/10)**3.98 + 30*(m.capacity + 1.2)
    print(controlled_velocity)

ambulance1(myAmbulance)
