# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 00:12:58 2018

@author: maref
"""

#x = 42
low = 0
high = 100
guess = int((low + high)/2)
text = "h", "l", "c"
print("Please think of a number between 0 and 100!")

while text != "c":
    print("Is your secret number ", int(guess), "?")
    text = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    
    if text == 'l':
        low = guess
        guess = int((low + high)/2)

    elif text == 'h':
        high = guess
        guess = int((low + high)/2)

    elif text == 'c':
        print("Game over. Your secret number was: ", int(guess))
        
    else:
        print("Sorry, I did not understand your input.")

    #guess = (low + high)/2

    
    
#print("Is your secret number " + str(round(guess,)) + "?")
    
    
