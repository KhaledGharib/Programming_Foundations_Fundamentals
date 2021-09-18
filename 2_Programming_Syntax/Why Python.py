# this code will gonna ask you for the name and age 
# then if the age bigger than 16 will print —> Feel free to join , 
# khaeld. or will print —> You're too young to register, khaled.

name  = input ("Hi, what's your name? ")
age = int (input ("How old are you? "))

if(age < 16):
    print ("You're too young to register ",name)
else:
    print ("Feel free to join ",name)