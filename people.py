import random
from data import *
import string

class People:
    def __init__(self):
        self.givenName = random.choice(givenName)
        self.familyName = random.choice(familyName)
        self.sex = random.choice(['M','F'])
        self.expDate = f'{date[0]}/{date[1]}/{date[2]}'
        self.id = ''.join(random.choices(string.ascii_uppercase, k=8))
        self.pGivenName = self.givenName
        self.pFamilyName = self.familyName
        self.pExpDate = self.expDate
        self.pId = self.id
        self.reason = random.choice(['Work', 'Transit', 'Entertainment', 'Coup d\'état', 'Terrorism', 'Refugee'])
        self.duration = random.randint(3,30)
        self.tag = 'people'

class Expired:
    def __init__(self):
        self.givenName = random.choice(givenName)
        self.familyName = random.choice(familyName)
        self.sex = random.choice(['M','F'])
        self.expDate = f'{date[0]}/{date[1]}/{date[2]}'
        self.id = ''.join(random.choices(string.ascii_uppercase, k=8))
        self.pGivenName = self.givenName
        self.pFamilyName = self.familyName
        self.pExpDate = f'{date[0] + random.randint(1,4)}/{date[1] + random.randint(0,2)}/{date[2] + random.randint(0,1)}'
        self.pId = self.id
        self.reason = random.choice(['Work', 'Transit', 'Entertainment', 'Coup d\'état', 'Terrorism', 'Refugee'])
        self.duration = random.randint(3,30)
        self.tag = 'expired'

class Imposter:
    def __init__(self):
        self.givenName = random.choice(givenName)
        self.familyName = random.choice(familyName)
        self.sex = random.choice(['M','F'])
        self.expDate = f'{date[0]}/{date[1]}/{date[2]}'
        self.id = ''.join(random.choices(string.ascii_uppercase, k=8))
        self.pGivenName = imposterName[random.randint(0,len(imposterName)-1)]
        self.pFamilyName = self.familyName
        self.pExpDate = f'{date[0] + random.randint(1,4)}/{date[1] + random.randint(0,2)}/{date[2] + random.randint(0,1)}'
        self.pId = self.id
        self.reason = random.choice(['Work', 'Transit', 'Entertainment', 'Coup d\'état', 'Terrorism', 'Refugee'])
        self.duration = random.randint(3,30)
        self.tag = 'imposter'

class Identity:
    def __init__(self):
        self.givenName = random.choice(givenName)
        self.familyName = random.choice(familyName)
        self.sex = random.choice(['M','F'])
        self.expDate = f'{date[0]}/{date[1]}/{date[2]}'
        self.id = ''.join(random.choices(string.ascii_uppercase, k=8))
        self.pGivenName = self.givenName
        self.pFamilyName = self.familyName
        self.pExpDate = f'{date[0] + random.randint(1,4)}/{date[1] + random.randint(0,2)}/{date[2] + random.randint(0,1)}'
        self.pId = ''.join(random.choices(string.ascii_uppercase, k=8))
        self.reason = random.choice(['Work', 'Transit', 'Entertainment', 'Coup d\'état', 'Terrorism', 'Refugee'])
        self.duration = random.randint(3,30)
        self.tag = 'identity'
