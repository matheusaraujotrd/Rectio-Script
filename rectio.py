import pyperclip
import os
import time

def key_error_command():
    decision = 0
    print("No character available for conversion. You probably typed the wrong character.\n")
    print("1. Try again\n Type any other character to exit.")
    decision = int(input())
    if decision == 1:
        main()

def turkish_convert():
    continue_function = 1
    while continue_function == 1:
        print("Type the character to convert:\n")
        try:
            convert_char = input()
            print("Character converted to " + Turkey[convert_char])
        except KeyError():
            key_error_command()
        pyperclip.copy(Turkey[convert_char])
        print("Copied to clipboard")
        print("1. Continue conversion\n2. Return to countries list\n3. Exit\n")
        continue_function = int(input())
        if continue_function == 2:
            os.system("cls")
            main()
def main():
    decision = 0
    while decision not in countries_support:
        print("1. Turkey\n2. Germany (WIP)\n")
        decision = int(input())
        if decision not in countries_support:
            os.system("cls")
            print("Wrong input! Try again.")
            time.sleep(3)
        os.system("cls")
    if decision == 1:
        turkish_convert();

countries_support = (1, 1)
Turkey = {"C":"Ç", "S":"Ş", "G":"Ğ", "O":"Ö", "U":"Ü", "I":"İ", "i":"ı", "g":"ğ", "u":"ü", "c":"ç", "s":"ş"}
main()
