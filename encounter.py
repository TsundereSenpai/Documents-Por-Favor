from people import *
import random

def Encounter():
    seed = random.randint(0,15)

    match seed:
        case 0:
            return Expired()
        case 1:
            return Imposter()
        case 2:
            return Identity()
        case _:
            return People()
