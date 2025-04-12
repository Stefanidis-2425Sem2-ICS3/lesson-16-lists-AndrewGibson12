#Name:A.Gibson
#Title:Average of numbers
#Date:April 12, 2025
#Description:This program generates 100 random numbers then finds the average
import random

numbers = []#get list
for i in range(0, 100):
    num = random.randint(0,100)
    (numbers.append(num))#add to list
print(numbers)#print list
average=sum(numbers)/100#get average
print(average)#print the average