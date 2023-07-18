#module importing
from encode_decode import *
from unit_testing import EmptyError, InputError


#main menu
print("Welcome to EDCODE, the best encode/decode tool since the Enigma!")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

def menu():
  available_operations = ["Encode a message", "Decode a message", "Strong encode", 
  "Strong decode", "Exit the program"]

  for i, option in enumerate(available_operations):
    print(f"{i+1}. {option}")


#asking for option
def ask_choice():
  choice = input("\nEnter the number of desired option: ")
  if not choice: raise InputError 
  return choice


#asking for string input
def ask_input(choice):
  if choice == 1: option = "encode"
  elif choice == 2: option = "decode"
  elif choice == 3: option = "strong encode"
  elif choice == 4: option = "strong decode"
  else: raise InputError 

  string = input(f"Please enter the string you wish to {option}!\n\nYour string: ")
  print("")

  return string



#main loop
while True:
  string = ""
  setting = ""

  menu()
  try:
    choice = int(ask_choice()) 
    if choice != 5: string = ask_input(choice)

    #call the desired function
    if choice == 1:
      if string =="": raise EmptyError #checking if the string is empty
      else:
        encoded_string = encode(string)
        print(f"Encoded string: {encoded_string}")

    elif choice == 2:
      if string =="": raise EmptyError #checking if the string is empty
      else:
        decoded_string = decode(string)
        print(f"Decoded string: {decoded_string}")

    elif choice == 3:
      if string =="": raise EmptyError #checking if the string is empty
      else:
        encoded_string, setting = strong_encode(string)
        print(f"Encoded string: {encoded_string} and decode setting is {setting}!")

    elif choice == 4:
      if string =="": raise EmptyError #checking if the string is empty
      else:
        setting = input("Enter the setting you were given at the time of encoding: ")
        decoded_string = strong_decode(string, setting)
        print(f"Decoded string: {decoded_string}")

    elif choice == 5:
      break

  #different errors testing
  except InputError as error:
    print("Wrong input! Only 1-3 available!")
    continue

  except EmptyError as error:
    print("Entered string was empty!")
    continue

  finally:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

print("Exiting the program...")