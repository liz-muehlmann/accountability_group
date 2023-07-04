# a program that generates a random whole number
import random

low = int(input("Enter the lower bound number: "))
high = int(input("Enter the upper bound number: "))

print(random.randrange(low,high))