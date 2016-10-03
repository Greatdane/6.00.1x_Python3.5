# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 08:41:51 2016

@author: davidwilson
"""

high = 100
low = 0
guess = int((high + low)/2)
user_input = ""
print("Please think of a number between 0 and 100!")

while user_input != "c":    
    print("Is your secret number " + str(guess))
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' \
    to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if user_input == "c":
        print("Game over. Your secret number was: " + str(guess))
        break
    elif user_input == "h":
        high = guess
        guess = int((high + low)/2)
    elif user_input == "l":
        low = guess
        guess = int((high + low)/2)
    else:
        print("Sorry, I did not understand your input.")
