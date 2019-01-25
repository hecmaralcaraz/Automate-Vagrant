#!/usr/bin/python
# Hèctor Martínez
# 23/01/2019

# This program autamate the creating vagrant machines.

import os

# Variables

global ip
name_OS = str("")
hostname = str("")
menu_network = int(0)

# Funtions

def list_box():
    '''List a vagrant boxes'''
    print("List of OS:")
    print("##############")
    os.system("vagrant box list")  # comand to list vagrant boxes
    print("")

def add_box():
    '''Add a new box'''
    Box = str("")
    y = bool(0)
    
    while y == 0:
        x = input ("Do you want add a NEW operating system? (no|yes)\n> ")  # if you need a new vagrant box
        if x == "yes":
            print("\nSearch in the following link")
            print("https://app.vagrantup.com/boxes/search")  # link to database vagrant boxes
            Box = input("Add a new box name \n>")
            os.system("vagrant box add "+Box)  # comand to add a new vagrant box
            os.system("clear")  # clear screen
            list_box()
            y = 1
        if x == "no":
            y = 1

def menu_network_box():
    '''Select network interface'''
    net_option = int(0)
    #Menu network
    print ("You can select a new network interface")
    print ("\nType de number of the option that you want to take")
    print ("1 Internal network")
    print ("2 Host-Only with DHCP")
    print ("3 Host-Only with static IP")
    print ("4 Bridge with DHCP\n")
    net_option = input("> ")
    return net_option

def internal_network():
    '''Conf internal network interface'''
    ip = str("")
    ip = input("What IP do you want?\n> ")
    name_opt = input("Need you a specific name for the private network? (yes|no)\n> ")
    if name_opt == "yes":
        name = input("What name do you want?\n> ");

# Structure


list_box()
add_box()
name_OS = input("What operating sistem do you want? \n> ")
hostname = input("What hostname do you want? \n> ")
menu_network = menu_network_box()

if menu_network == 1:
    internal_network()
elif menu_network == 2:
    print ("2")
elif menu_network == 3:
    print ("3")
elif menu_network == 4:
    print ("4")
    
print (ip)
print("END")












