#Module 4-4
import random

code=random.randint(1,10)
password = int(input("Please enter the password(1-10):"))
while password>0:

        if password>code:
           print("Too high.")
           password = int(input("Please enter the password(1-10):"))


        elif password<code:
            print("Too low.")
            password = int(input("Please enter the password(1-10):"))

        else:
            print("Correct.")
            break

