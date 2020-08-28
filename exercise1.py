#Create a program that asks user to enter their name and age
#The output tells user in what year they will be 100 years old

from datetime import datetime
current_year = datetime.now().year

name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((current_year - age)+100)
print("The current year is " + str(current_year) + ", therefore...")
print(name + ", you will be 100 years old in the year " + year + "!")




