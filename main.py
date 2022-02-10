from people import *
from data import *
from encounter import *
from judgment import *
import time
import colorama
import os

colorama.init()
counter = 0

while True:
    #variables
    customer = Encounter()

    os.system('cls' if os.name == 'nt' else 'clear')

    print(f'''
    Welcome to {colorama.Fore.BLUE}Documents, Por Favor.\033[39m Today is {date[0]}/{date[1]}/{date[2]}.
    people processed: {counter}

    Documents, Por Favor.
    ''')

    print(f'''
    Passport

    Name: {customer.familyName}, {customer.givenName}
    Sex: {customer.sex}
    ID: {customer.id}
    Exp.: {customer.expDate}

    ''')

    print(f'''
    Enter Permit

    Name: {customer.pFamilyName}, {customer.pGivenName}
    ID: {customer.pId}
    Exp.: {customer.pExpDate}
    Purpose: {customer.reason}
    Duration: {customer.duration} Days
    ''')

    print(f'{colorama.Fore.RED}Reject? {colorama.Fore.GREEN} Accept? \033[39m')
    response = input('Judgment: ').lower()
    print(response)
    if Judgment(response, customer) == False:
        match customer.tag:
            case "people":
                print("that was an innocent person!")
            case 'expired':
                print('that was a fake/expired date!')
            case 'identity':
                print('that ID didn\'t match!')
            case 'imposter':
                print('the name didn\'t match!')
        print('Game Over!')
        break
    if Judgment(response, customer) == True:
        counter += 1
