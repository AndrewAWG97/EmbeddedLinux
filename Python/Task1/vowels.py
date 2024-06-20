#!/bin/python3

def CheckVowel():
    vowels_ls = ['a', 'o', 'i', 'u', 'e']
    char =  input("Enter a letter : ")
    for i in vowels_ls:
        if char == i:
            return True
    return False

while True:
    if(CheckVowel()):
        print("Vowel")
    else:
        print("Not Vowel")