#!/usr/bin/python
# Hèctor Martínez
# 23/01/2019

# This program autamate the creating vagrant machines.

import os

# Variables

nameOS = str("")
hostname = str("")

# Funtions

def listbox():
    '''List a vagrant boxes'''
    print("List of OS:")
    print("##############")
    os.system("vagrant box list")  # comand to list vagrant boxes
    print("")

def addbox():
    '''Add a new box'''
    Box = str("")
    y = bool(0)
    
    while y == 0:
        x = input ("Do you want add a NEW operating system? (no|yes)\n>")  # if you need a new vagrant box
        if x == "yes":
            print("\nSearch in the following link")
            print("https://app.vagrantup.com/boxes/search")  # link to database vagrant boxes
            Box = input("Add a new box name \n>")
            os.system("vagrant box add "+Box)  # comand to add a new vagrant box
            os.system("clear")  # clear screen
            listbox()
            y = 1
        if x == "no":
            y = 1
            
def networkbox():
    '''Select network interface'''
    print ("test network")
    
    
# Structure

listbox()
addbox()
nameOS = input("What operating sistem do you want? \n>")
hostname = input("What hostname do you want? \n>")
networkbox()













