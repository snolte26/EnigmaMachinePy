import os
import time
from termcolor import colored


def machine():
    # SETTING ROTORS, REFLECTORS, AND BASE
    rotorBase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    rotor1 = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A',
              'I', 'B', 'R', 'C', 'J']
    rotor2 = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P',
              'Y', 'F', 'V', 'O', 'E']
    rotor3 = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K',
              'M', 'U', 'S', 'Q', 'O']
    rotor4 = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K',
              'D', 'C', 'M', 'W', 'B']
    rotor5 = ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q',
              'O', 'F', 'E', 'C', 'K']
    reflector1 = ['E', 'J', 'M', 'Z', 'A', 'L', 'Y', 'X', 'V', 'B', 'W', 'F', 'C', 'R', 'Q', 'U', 'O', 'N', 'T', 'S',
                  'P', 'I', 'K', 'H', 'G', 'D']
    reflector2 = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z',
                  'C', 'W', 'V', 'J', 'A', 'T']
    reflector3 = ['F', 'V', 'P', 'J', 'I', 'A', 'O', 'Y', 'E', 'D', 'R', 'Z', 'X', 'W', 'G', 'C', 'T', 'K', 'U', 'Q',
                  'S', 'B', 'N', 'M', 'H', 'L']

    '''
    rotorBase = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

    rotor1 = [10, 7, 4, 17, 15, 24, 21, 19, 3, 1, 13, 9, 6, 18, 22, 20, 16, 14, 5, 23, 11, 2, 12, 26, 25, 8]
    rotor2 = [14, 20, 26, 16, 19, 6, 2, 15, 11, 13, 23, 18, 3, 10, 4, 9, 22, 12, 1, 5, 25, 21, 24, 8, 7, 17]
    rotor3 = [10, 22, 9, 21, 2, 8, 20, 3, 4, 25, 1, 11, 5, 17, 26, 16, 15, 19, 7, 24, 14, 18, 13, 23, 6, 12]
    rotor4 = [17, 25, 8, 15, 7, 14, 5, 3, 22, 16, 21, 26, 20, 6, 4, 10, 1, 24, 23, 13, 11, 9, 19, 18, 2, 12]
    rotor5 = [17, 23, 5, 18, 20, 26, 21, 9, 15, 1, 19, 4, 6, 7, 8, 10, 11, 16, 25, 24, 3, 22, 2, 14, 13, 12]
    ['Q', 'Y', 'H', 'O', 'G', 'N', 'E', 'C', 'V', 'P', 'U', 'Z', 'T', 'F', 'D', 'J', 'A', 'X', 'W', 'M', 'K', 'I', 
    'S', 'R', 'B', 'L']
    '''

    # LIST OF ROTORS AND REFLECTORS
    rotorList = [rotor1, rotor2, rotor3, rotor4, rotor5]
    reflectorList = [reflector1, reflector2, reflector3]

    # CREATING FILE TO SAVE SETTINGS
    settings = open("emSettings.txt", "w+")

    # CHOOSING WHICH ROTORS, REFLECTOR, AND ROTOR STARTING POSITION TO USE
    while True:
        rotorChoice1 = int(input("First rotor, 1-5: ")) - 1
        rotorSetting1 = int(input("Enter position of rotor 1, 1-26: "))
        os.system('cls')
        rotorChoice2 = int(input("Second rotor, 1-5: ")) - 1
        rotorSetting2 = int(input("Enter position of rotor 2, 1-26: "))
        os.system('cls')
        rotorChoice3 = int(input("Third rotor, 1-5: ")) - 1
        rotorSetting3 = int(input("Enter position of rotor 3, 1-26: "))
        os.system('cls')
        reflector = int(input("Which reflector, 1-3: ")) - 1
        os.system('cls')

        # CHECKING IF EACH ROTOR IS UNIQUE
        if rotorChoice2 == rotorChoice1 or rotorChoice3 == rotorChoice1 or rotorChoice2 == rotorChoice3:
            print("Each rotor must be unique")
            continue
        else:
            # WRITE ROTOR AND REFLECTOR SETTINGS TO THE FILE
            settings.writelines("Rotors: " + (str(rotorChoice1 + 1) + "-" + str(rotorSetting1)) + ", " + (
                        str(rotorChoice2 + 1) + "-" + str(rotorSetting2)) + ", " + (
                                            str(rotorChoice3 + 1) + "-" + str(rotorSetting3)) + "\n")
            settings.writelines("Reflector: " + str(reflector + 1) + "\n")

            # SETTING THE ROTOR CHOICES
            rotorChoice1 = rotorList[rotorChoice1]
            rotorChoice2 = rotorList[rotorChoice2]
            rotorChoice3 = rotorList[rotorChoice3]
            reflector = reflectorList[reflector]
            break

    # SETS THE ROTOR STARTING POSITIONS
    for i in range(rotorSetting1):
        rotorChoice1 += [rotorChoice1.pop(0)]

    for i in range(rotorSetting2):
        rotorChoice2 += [rotorChoice2.pop(0)]

    for i in range(rotorSetting3):
        rotorChoice3 += [rotorChoice3.pop(0)]

    # SET PLUG LIST
    plugList = []
    plugs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']

    # GETS LETTERS TO PAIR, CHECKS IF USED ALREADY, AND ADDS THEM TO PLUG PAIR LIST
    for i in range(10):
        while True:
            breakout = True
            firstLetter = str(input("Enter first letter: "))
            os.system('cls')
            secondLetter = str(input("Enter second letter: "))
            os.system('cls')
            # IF THE PLUG IS NOT IN THE PLUG LIST, YOU CANNOT USE IT
            if firstLetter.upper() not in plugs or secondLetter.upper() not in plugs:
                print("1 or more letters is already in use")
                breakout = False
            # OTHERWISE, REMOVE THEM FROM USABLE PLUGS LIST AND SET AS A PAIR IN THE PLUG PAIR LIST
            if firstLetter.upper() in plugs and secondLetter.upper() in plugs:
                plugs.remove(firstLetter.upper())
                plugs.remove(secondLetter.upper())
                pair = firstLetter.upper() + secondLetter.upper()
                plugList.append(pair)
                breakout = True
            if breakout:
                break
            else:
                continue

    # WRITE THE PLUG BOARD TO THE FILE AND CLOSE THE FILE
    settings.writelines("Plug Board: " + str(plugList))
    settings.close()

    # GETS MESSAGE TO ENCODE, CAPITALIZES, AND REMOVES SPACES
    message = input("Message to Process: ")
    os.system('cls')
    message = message.upper()
    messageList = list(message)

    for item in messageList:
        if item not in rotorBase:
            messageList.remove(item)

    encodedList = []
    rotor1Count = 0
    rotor2Count = 0
    rotor3Count = 0

    keyboardList = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '\n', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                    '\n', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '\n']

    for item in messageList:

        # IF THE CURRENT LETTER IN THE MESSAGE HAS A PLUG PAIR, CHANGE THE LETTER TO THE PAIRED LETTER
        for i in range(len(plugList)):
            if item in plugList[i]:
                letters = plugList[i]

                for j in letters:
                    if j == item:
                        item = letters.replace(j, '')
                        break

            else:
                continue

        itemLetter = item

        # MOVE EACH ROTOR 1 SPOT THE PREVIOUS ROTOR HAS MOVED 26 TIMES
        rotorChoice1 += [rotorChoice1.pop(0)]
        if rotor1Count == 26:
            rotor2Count += 1
            rotorChoice2 += [rotorChoice2.pop(0)]
            rotor1Count = 0
            if rotor2Count == 26:
                rotor3Count += 1
                rotorChoice3 += [rotorChoice3.pop(0)]
                rotor2Count = 0

        # FOR EACH LETTER IN THE CHOSEN ROTOR
        # IF THE THE CURRENT LETTER IN THE MESSAGE IS EQUAL TO THE ROTOR LETTER
        # GET THE INDEX OF THE ROTOR LETTER
        # CHANGE THE MESSAGE LETTER TO THE ROTOR BASE LETTER AT SAME INDEX
        # BREAK, REPEAT THROUGH REFLECTOR
        for letter in rotorChoice1:
            if itemLetter == letter:
                objIndex = rotorChoice1.index(letter)
                itemLetter = rotorBase[objIndex]
                break
        for letter in rotorChoice2:
            if itemLetter == letter:
                objIndex = rotorChoice2.index(letter)
                itemLetter = rotorBase[objIndex]
                break
        for letter in rotorChoice3:
            if itemLetter == letter:
                objIndex = rotorChoice3.index(letter)
                itemLetter = rotorBase[objIndex]
                break
        for letter in reflector:
            if itemLetter == letter:
                objIndex = reflector.index(letter)
                itemLetter = rotorBase[objIndex]
                break

        # FOR EACH LETTER IN THE CHOSEN ROTOR
        # IF THE THE CURRENT LETTER IN THE MESSAGE IS EQUAL TO THE ROTOR LETTER
        # GET THE INDEX OF THE ROTOR BASE LETTER
        # CHANGE THE MESSAGE LETTER TO THE ROTOR LETTER AT SAME INDEX
        # BREAK, REPEAT THROUGH FIRST ROTOR
        for letter in rotorChoice3:
            if itemLetter == letter:
                objIndex = rotorBase.index(letter)
                itemLetter = rotorChoice3[objIndex]
                break
        for letter in rotorChoice2:
            if itemLetter == letter:
                objIndex = rotorBase.index(letter)
                itemLetter = rotorChoice2[objIndex]
                break
        for letter in rotorChoice1:
            if itemLetter == letter:
                objIndex = rotorBase.index(letter)
                itemLetter = rotorChoice1[objIndex]
                break

        # INCREASE FIRST ROTOR COUNT BY 1
        rotor1Count += 1
        print("     " + str(rotorChoice3[0]) + " " + str(rotorChoice2[0]) + " " + str(rotorChoice1[0]))

        # IF THE CURRENT LETTER IN THE MESSAGE HAS A PLUG PAIR, CHANGE THE LETTER TO THE PAIRED LETTER
        for i in range(len(plugList)):
            if itemLetter in plugList[i]:
                letters = plugList[i]

                for j in letters:
                    if j == itemLetter:
                        itemLetter = letters.replace(j, '')
                        break

            else:
                continue

        # ADD THE ENCODED MESSAGE LETTER TO THE ENCODED MESSAGE LIST
        encodedList.append(itemLetter)

        print()
        keyboardList = "".join(keyboardList)
        for i in range(len(keyboardList)):
            if keyboardList[i] == itemLetter:
                print(colored(keyboardList[i], 'blue', 'on_yellow'), end=" ")
            else:
                print(keyboardList[i], end=" ")
        time.sleep(.2)
        os.system('cls')

    # JOIN THE ENCODED MESSAGE LIST INTO 1 STRING
    print("     " + str(rotorChoice3[0]) + " " + str(rotorChoice2[0]) + " " + str(rotorChoice1[0]))
    print()
    keyboardList = "".join(keyboardList)
    for i in range(len(keyboardList)):
        print(keyboardList[i], end=" ")
    print()
    print("Message: " + "".join(encodedList))


def main():
    while True:
        machine()
        choice = int(input("1 to continue, 0 to quit: "))
        if choice == 1:
            continue
        elif choice == 0:
            break


main()
