# TODO:  program to create a dictionary of numbers and their squares as a key value pair respectively for all the numbers below the specified input.

a = int(input("enter the number"))
d = {}
for i in range(a):
    j = i+1
    d[j] = j**2
print(d)