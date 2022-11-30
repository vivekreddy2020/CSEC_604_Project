import sys
from feed import start_app
from cryptic import *


def start():
    
    print("Options: For Encryption with facial biometrics, press 'E' ")
    print("         For Decryption, press 'D' ")
    print("         To exit program, press 'X' ")
    put = input()
    if put == 'E':
        encryption_proc()
    elif put == 'D':
        decryption_proc()
    elif put == 'X':
        sys.exit("Program terminated!")
    else:
        print("Wrong options entered. \n")
        start()

def encryption_proc():
    print("Enter File name: \n")
    path = input()
    if check(path):
        print("File is already encrypted, returning to main menu\n")
        start()
    else:
        if encrypting(start_app(), path) is True:
            print("File has been encrypted successfully!!\n")

            start()
        else: 
            print("Error encrypting the current file format, returning to main menu.")
            start()
def decryption_proc():
    print("Enter File name: \n")
    path = input()
    if check(path) == False:
        print("File is already Decrypted\n")
        start()
    else:
        if decrypting(start_app(), path) is True:
            print("File has been decrypted succesfully!!, returning to main menu.\n")
            start()
        else:
            i = input("Decryption failed with current face id!, Do you want to try again (Y)es or (N)o\n")
            if i == 'Y':
                decryption_proc()
            if i == 'N':
                sys.exit("Terminating program!!")


if __name__ == '__main__':
    print("Welcome, this is a test program to check the deployment!! \n")
    start()