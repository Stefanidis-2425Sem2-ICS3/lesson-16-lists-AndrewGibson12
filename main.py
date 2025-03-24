# Name: A. Gibson
# Title: Average
# Date: march 24, 2025
# Description: This program takes 100 random numbers then finds the average
import random
num={random.randint(0,100) for i in range(100)}

print("Your 100 numbers are,")
print(num)

Average = sum(num)/len(num)
print("The average of the 100 numbers is", Average)