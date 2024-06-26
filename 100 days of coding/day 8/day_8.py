

'''
Author : Je Nolan 
6/13/2024



Program uses Ceaser Cypher.

Provides a header;

Ask the user if they want to encode or decode.
'''


'''
Encode function change message by shifting the alphabet letters over by the number requested 
i.e. 
The player asks for the message
then the player is asked for the shifted nuber
i.e.
if the message is "ABC" and the number shifted is 3 the new message becomes
DEF (A(0)-->D(3), B(1)-->E(4), and C(2)-->F(5))

'''


#logo

from secrets import choice


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


#ask for message to encode and number of shifts
def encode ():
    message = input("What is your message. \t")
    num_shift = int(input("Type the shift number."))


#ask for the message to decode and number of shifts
def decode():
    message = input("What is your message. \t")
    num_shift = int(input("Type the shift number."))

print(logo)
alphabet = ['a','b','c','d']

end_of_program = False #initial variable assignment
#conduct a while statement that will continue the program until the player types no into the input box

#continue program until the player chooses the no option
while end_of_program == False:
    choice = input("Type 'encode' to encrypt, 'decode' to decrypt\n").lower()
   #based upon choice call corresponding function 
    if choice == "encode":
        encode()
    else:
        decode()
    continue_choice = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if continue_choice == 'yes':
        continue
    else:
        end_of_program = True

    
