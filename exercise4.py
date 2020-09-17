# Generate a random password with length "password_length"   
# No duplicate characters 
# No special characters
# No spaces

import random

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890"
password_length = 10
my_new_password =  "".join(random.sample(char, password_length))
print(my_new_password)