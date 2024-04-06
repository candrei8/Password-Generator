import random #random library 
import string #to take all the numbers, chars and letters from a library instead of writing them down

#letters numbers and special chars
letters = string.ascii_letters
numbers = string.digits
characters = string.punctuation

#The lenght of the passowrd depending on the imput
lenght = int(input("Enter the password lenght: "))

#specifying how the password has to be
chars = letters
chars += numbers 
chars += characters

#Password 
pwd = ""

#Create the password depending on the specified lenght
for i in range(lenght):
    new_char = random.choice(chars)
    pwd += new_char

print("This is your password: ",pwd)