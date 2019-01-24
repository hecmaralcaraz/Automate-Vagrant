#!/usr/bin/python
# Hèctor Martínez
# 23/01/2019

# This programat autamate the creating vagrant's machines.

import os

# Variables

nameOS = str("")
hostname = str("")

# Funtions

def listarbox():
    print("Lista de OS:")
    print("##############")
    os.system("vagrant box list")
    print("")

def añadirbox():
    Box = str("")
    x = input ("Quieres añadir un sistema operativo nuevo? (si|no)")
    if x == "si":
        print("Busca en el siguiente enlace: ")
        print("https://app.vagrantup.com/boxes/search")
        Box = input("Introduce el nombre de la nueva Box \n")
        os.system("vagrant box addi "+Box)
        

 
# Structure

listarbox()

añadirbox()
os.system("clear")

nameOS = input("Que sistema operativo quieres? \n")
hostname = input("Que hostname quieres? \n")


