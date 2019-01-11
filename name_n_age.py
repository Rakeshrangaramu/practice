# TODO:Create a program that asks the user to enter their name and their age.
# TODO:Print out a message addressed to them that tells them the year that they will turn 100 years old

name = input("Enter the name ")
age =int(input("enter the age "))
year = 2019
age_After_100_yrs = year+100-age
print(age_After_100_yrs)
print('Hi',name,'! Your age after 100 years is ', age_After_100_yrs)