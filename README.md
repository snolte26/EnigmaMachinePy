# EnigmaMachinePy
A command line recreation of the Enigma Machine

From Wikipedia:
The Enigma machine is a cipher device developed and used in the early- to mid-20th century to protect commercial, diplomatic, and military communication. It was employed extensively by Nazi Germany during World War II, in all branches of the German military. The Germans believed, erroneously, that use of the Enigma machine enabled them to communicate securely and thus enjoy a huge advantage in World War II. The Enigma machine was considered to be so secure that even the most top-secret messages were enciphered on its electrical circuits.

https://en.wikipedia.org/wiki/Enigma_machine

The enigmaMachine.py has multiple possible combinations of settings for writing a message. Users can pick 3 rotors out of 5, 1 reflector out of 3, 1 of 26 starting positions for each rotor, and create 10 pairs of letters much like on the plugboard of an actual Enigma Machine.

The resulting amount of possible settings combinations calculates out to 476,887,665,653,479,080,000, or about 477 Quintillion

Math:


(5 * 4 * 3) (26^3) (3) = 3,163,680 possible rotor/reflector combinations

(26!) / (6! * 10! * 2^10) = 150,738,274,937,250 possible plugboard combinations

3,163,680 * 150,738,274,937,250 = 476,887,665,653,479,080,000 Total possible combinations on this Enigma Machine


Rather than having to encode 1 letter at a time like the original machine, you input your initial settings, type to full message out, and the machine spits out the processed message. Using the same settings as when you encoded a message, you can decrypt a message in the same way

When setting the rotors and plug board, all settings are hidden so that no one can peep over your shoulder and see the settings, and the same thing goes for the initial message.

Download the dist folder to begin using the machine

The Enigma Machine now writes your settings to a file that can be called later. Users no longer have to write down their settings manually.

Pucntuation and spaces are removed from the original message, to throw off any code-breaking by grammar conventions. Numbers are not encoded like the rest of the message, do NOT use numbers expecting things to go smoothly

EnigmaMachinePY now has a user interface! Just run EnigmaMachineGUI to use the interface. Interface uses Tkinter, and allso you to change settings easily in your machine and outputs the message in the console
