import os
import time
import tkinter as tk
# import tkinter.scrolledtext
from tkinter import *
from tkinter import ttk

# from tkinter.messagebox import showinfo
# from termcolor import colored

root = tk.Tk()
root.geometry('900x550')
root.resizable(True, True)
root.title('Enigma Machine')
root.minsize(900, 550)
root.rowconfigure(2, weight=4)

rotorDisplay = ttk.Label(root, text="", font=("Helvetica", 14))
rotorDisplay.grid(column=1, row=2, columnspan=4, padx=10)
lights = Text(root, font=("Helvetica", 14), height=3)
lights.grid(column=1, row=3, columnspan=4, padx=10)


def machine():
    print()
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
    keyboardList = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '\n', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                    '\n', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '\n']
    # plugs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    # 'U', 'V', 'W', 'X', 'Y', 'Z']
    rotorList = [rotor1, rotor2, rotor3, rotor4, rotor5]
    reflectorList = [reflector1, reflector2, reflector3]
    reflect = int(float(selected_reflector.get()))
    rot1 = int(float(selected_rotor1.get()))
    rot2 = int(float(selected_rotor2.get()))
    rot3 = int(float(selected_rotor3.get()))

    rotorSetting1 = int(rotor1_position.get())
    rotorSetting2 = int(rotor2_position.get())
    rotorSetting3 = int(rotor3_position.get())

    rotorChoice1 = rotorList[rot1]
    rotorChoice2 = rotorList[rot2]
    rotorChoice3 = rotorList[rot3]
    reflector = reflectorList[reflect]

    for i in range(rotorSetting1):
        rotorChoice1 += [rotorChoice1.pop(0)]

    for i in range(rotorSetting2):
        rotorChoice2 += [rotorChoice2.pop(0)]

    for i in range(rotorSetting3):
        rotorChoice3 += [rotorChoice3.pop(0)]
    plugList = [plugPair1.get().upper(), plugPair2.get().upper(), plugPair3.get().upper(), plugPair4.get().upper(),
                plugPair5.get().upper(),
                plugPair6.get().upper(), plugPair7.get().upper(), plugPair8.get().upper(), plugPair9.get().upper(),
                plugPair10.get().upper()]
    message = msg.get()

    message = message.upper()
    messageList = list(message)

    for item in messageList:
        if item not in rotorBase:
            messageList.remove(item)

    encodedList = []
    rotor1Count = 0
    rotor2Count = 0
    rotor3Count = 0

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
        rotorMSG = ("     " + str(rotorChoice3[0]) + " " + str(rotorChoice2[0]) + " " + str(rotorChoice1[0]) + "\n")

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

        # print(rotorMSG)
        keyboardList = "".join(keyboardList)
        for i in range(len(keyboardList)):
            if keyboardList[i] == itemLetter:
                # print(colored(keyboardList[i], 'blue', 'on_yellow'), end=" ")
                idx = i
                if 0 <= idx < 10:
                    startingIndex = "1." + str(idx)
                    endingIndex = "1." + str(idx + 1)
                    if endingIndex == "1.10":
                        endingIndex = "2.0"
                elif 11 <= idx < 20:
                    startingIndex = "2." + str(idx - 11)
                    endingIndex = "2." + str(idx - 10)
                    if endingIndex == "2.9":
                        endingIndex = "3.0"
                else:
                    startingIndex = "3." + str(idx - 21)
                    endingIndex = "3." + str(idx - 20)

            # else:
            # print(keyboardList[i], end=" ")
        rotorDisplay.config(text=rotorMSG)
        lights.delete('1.0', END)
        lights.tag_configure("center", justify='center')
        lights.insert(INSERT, keyboardList)
        lights.tag_add("center", 1.0, "end")
        lights.tag_config("lightUp", background="yellow")
        lights.tag_add("lightUp", startingIndex, endingIndex)
        rotorDisplay.update()
        lights.update()
        time.sleep(1)
        # os.system('cls')

    # JOIN THE ENCODED MESSAGE LIST INTO 1 STRING
    '''
    print("     " + str(rotorChoice3[0]) + " " + str(rotorChoice2[0]) + " " + str(rotorChoice1[0]))
    print()
    keyboardList = "".join(keyboardList)
    for i in range(len(keyboardList)):
        print(keyboardList[i], end=" ")
    print()
    '''
    print("Message: " + "".join(encodedList))


selected_rotor1 = tk.StringVar()
rotor1_position = tk.IntVar()
selected_rotor2 = tk.StringVar()
rotor2_position = tk.IntVar()
selected_rotor3 = tk.StringVar()
rotor3_position = tk.IntVar()
selected_reflector = tk.StringVar()
plugPair1 = tk.StringVar()
plugPair2 = tk.StringVar()
plugPair3 = tk.StringVar()
plugPair4 = tk.StringVar()
plugPair5 = tk.StringVar()
plugPair6 = tk.StringVar()
plugPair7 = tk.StringVar()
plugPair8 = tk.StringVar()
plugPair9 = tk.StringVar()
plugPair10 = tk.StringVar()
msg = tk.StringVar()
rotors = (('Rotor 1', '0'),
          ('Rotor 2', '1'),
          ('Rotor 3', '2'),
          ('Rotor 4', '3'),
          ('Rotor 5', '4'))
reflectors = (('Reflector 1', '0'),
              ('Reflector 2', '1'),
              ('Reflector 3', '2'))

frame1 = LabelFrame(
    root,
    text='Rotor 1'
)
frame1.grid(row=1, column=2, padx=10)
Radiobutton(frame1, text=rotors[0][0], variable=selected_rotor1, value=rotors[0][1]).pack()
Radiobutton(frame1, text=rotors[1][0], variable=selected_rotor1, value=rotors[1][1]).pack()
Radiobutton(frame1, text=rotors[2][0], variable=selected_rotor1, value=rotors[2][1]).pack()
Radiobutton(frame1, text=rotors[3][0], variable=selected_rotor1, value=rotors[3][1]).pack()
Radiobutton(frame1, text=rotors[4][0], variable=selected_rotor1, value=rotors[4][1]).pack()
Entry(frame1, textvariable=rotor1_position).pack(())

frame2 = LabelFrame(
    root,
    text='Rotor 2'
)
frame2.grid(row=1, column=3, padx=10)
Radiobutton(frame2, text=rotors[0][0], variable=selected_rotor2, value=rotors[0][1]).pack()
Radiobutton(frame2, text=rotors[1][0], variable=selected_rotor2, value=rotors[1][1]).pack()
Radiobutton(frame2, text=rotors[2][0], variable=selected_rotor2, value=rotors[2][1]).pack()
Radiobutton(frame2, text=rotors[3][0], variable=selected_rotor2, value=rotors[3][1]).pack()
Radiobutton(frame2, text=rotors[4][0], variable=selected_rotor2, value=rotors[4][1]).pack()
Entry(frame2, textvariable=rotor2_position).pack(())

frame3 = LabelFrame(
    root,
    text='Rotor 3'
)
frame3.grid(row=1, column=4, padx=10)
Radiobutton(frame3, text=rotors[0][0], variable=selected_rotor3, value=rotors[0][1]).pack()
Radiobutton(frame3, text=rotors[1][0], variable=selected_rotor3, value=rotors[1][1]).pack()
Radiobutton(frame3, text=rotors[2][0], variable=selected_rotor3, value=rotors[2][1]).pack()
Radiobutton(frame3, text=rotors[3][0], variable=selected_rotor3, value=rotors[3][1]).pack()
Radiobutton(frame3, text=rotors[4][0], variable=selected_rotor3, value=rotors[4][1]).pack()
Entry(frame3, textvariable=rotor3_position).pack()

frameReflect = LabelFrame(
    root,
    text='Reflector'
)
frameReflect.grid(row=1, column=1, padx=10)
Radiobutton(frameReflect, text=reflectors[0][0], variable=selected_reflector, value=reflectors[0][1]).pack()
Radiobutton(frameReflect, text=reflectors[1][0], variable=selected_reflector, value=reflectors[1][1]).pack()
Radiobutton(frameReflect, text=reflectors[2][0], variable=selected_reflector, value=reflectors[2][1]).pack()

framePair1 = LabelFrame(root, text='Pair 1')
framePair1.grid(row=4, column=1, pady=10)
Entry(framePair1, textvariable=plugPair1).pack()

framePair2 = LabelFrame(root, text='Pair 2')
framePair2.grid(row=4, column=2, padx=10)
Entry(framePair2, textvariable=plugPair2).pack()

framePair3 = LabelFrame(root, text='Pair 3')
framePair3.grid(row=4, column=3, padx=10)
Entry(framePair3, textvariable=plugPair3).pack()

framePair4 = LabelFrame(root, text='Pair 4')
framePair4.grid(row=4, column=4, pady=10)
Entry(framePair4, textvariable=plugPair4).pack()

framePair5 = LabelFrame(root, text='Pair 5')
framePair5.grid(row=5, column=1, padx=10)
Entry(framePair5, textvariable=plugPair5).pack()

framePair6 = LabelFrame(root, text='Pair 6')
framePair6.grid(row=5, column=2, padx=10)
Entry(framePair6, textvariable=plugPair6).pack()

framePair7 = LabelFrame(root, text='Pair 7')
framePair7.grid(row=5, column=3, pady=10)
Entry(framePair7, textvariable=plugPair7).pack()

framePair8 = LabelFrame(root, text='Pair 8')
framePair8.grid(row=5, column=4, padx=10)
Entry(framePair8, textvariable=plugPair8).pack()

framePair9 = LabelFrame(root, text='Pair 9')
framePair9.grid(row=6, column=2, padx=10)
Entry(framePair9, textvariable=plugPair9).pack()

framePair10 = LabelFrame(root, text='Pair 10')
framePair10.grid(row=6, column=3, pady=10)
Entry(framePair10, textvariable=plugPair10).pack()

frameMSG = LabelFrame(root, text='Message')
frameMSG.grid(row=7, column=2, pady=10, padx=10)
Entry(frameMSG, textvariable=msg).pack()

# button
button = ttk.Button(
    root,
    text="Submit",
    command=machine
)
button.grid(row=7, column=3, pady=10)

root.mainloop()
