import sys

from camera1 import start_app
from cryptic import *


def main():
    
    print("Options: For Encryption with facial biometrics, press 'E' \n")
    print("         For Decryption, press 'D' \n")
    put = input()
    if input == 'E':
        encryption_proc()
    if input == 'D':
        decryption_proc()

def encryption_proc():
    print("Enter File name: \n")
    path = input()
    if check(path):
        print("File is already encrypted, returning to main menu\n")
        main()
    else:
        if encrypt(start_app(), path):
            print("File has been encrypted successfully!!\n")
            main()
        else: 
            sys.exit("Error ouccred, Program terminated!!")

def decryption_proc():
    print("Enter File name: \n")
    path = input()
    if check(path) == False:
        print("File is already Decrypted\n")
        main()
    else:
        if decrypt(start_app(), path):
            print("File has been decrypted succesfully!!, returning to main menu.\n")
            main()
        else:
            i = input("Decryption failed with current face id!, Do you want to try again (Y)es or (N)o\n")
            if i == 'Y':
                decryption_proc()
            if i == 'N':
                sys.exit("Terminating program!!")


if __name__ == '__main__':
    print("Welcome, this is a test program to check the deployment!! \n")
    main()