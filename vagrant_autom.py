#!/usr/bin/python
# Hèctor Martínez
# 23/01/2019

# This program autamate the creating vagrant machines.

import os


# Variables

name_OS = str("")
hostname = str("")
menu_network = int(0)
ram= int(0)
ip = str("")
name_network = str("")


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
    print ("\nYou can select a new network interface")
    print ("\nType de number of the option that you want to take")
    print ("1 Internal network")
    print ("2 Host-Only with static IP")
    print ("3 Host-Only with DHCP")
    print ("4 Bridge with DHCP\n")
    net_option = input("> ")
    return net_option

def internal_network():
    '''Conf internal network interface'''
    global ip
    global name_network
    ip = input("\nWhat IP do you want?\n> ")
    name_opt = input("\nNeed you a specific name for the private network? (yes|no)\n> ")
    if name_opt == "yes":
        name_network = input("\nWhat name do you want?\n> ")
    elif name_opt == "no":
        name_network = "true"
    

def hostO_static():
    '''Conf Host-Only (static) network interface'''
    global ip
    ip = input("What IP do you want?\n> ")

def write_Vagrantfile(me_OS,hostname,menu_network,ip,name_network,ram):
    '''This funtion writes in Vagrantfile with variables that has been recolected'''
    try:
        file = open("Vagrantfile", "w")
    except FileNotFoundError:
        print("no se encuentra el archivo")

    file.write('Vagrant.configure("2") do |config|' + os.linesep)
    file.write('    config.vm.box = "' + name_OS + '"' + os.linesep)
    file.write('    config.vm.hostname = "' + hostname + '"' + os.linesep)
    file.write(os.linesep)
    if menu_network == '1':
        file.write('    config.vm.network "private_network", ip: "' + ip + '",' + os.linesep)
        file.write('    virtualbox__intnet: ' + name_network + os.linesep)
    elif menu_network == '2':
        file.write('    config.vm.network "private_network", ip: "' + ip + '"' + os.linesep)
    file.write('    config.vm.provider "virtualbox" do |vb|' + os.linesep)
    file.write('        vb.memory = "' + ram + '"' + os.linesep)
    file.write('    end' + os.linesep)
    file.write('end')

    file.close()


# Structure

list_box()  # List boxes
add_box()  # Add box
name_OS = input("\nWhat operating sistem do you want? \n> ")  # Name OS
hostname = input("\nWhat hostname do you want? \n> ")  # Hostname
menu_network = menu_network_box()  # menu to select network

# networfile.write('hola')
if menu_network == "1":  # if select internal network
    internal_network()
elif menu_network == "2":  # if select Host-Only with static IP
    hostO_static() 
print(menu_network)

ram = input("\nHow much RAM do you want?(autoselect: 1024) \n> ")
if ram == 0:
    ram = 1024
write_Vagrantfile(name_OS,hostname,menu_network,ip,name_network,ram)

print("**END**")


# name_os , hostname , menu_network , ip , name_network , ram
prueba1
