# TODO :a python program to print the key of a value given as a search element from a dictionary.

d = {'a':"Speckbit", 'b':"World", 'c':"Quiet"}
src =input("enter the search element: ")
for key in d:
    if src == d[key]:
        print("key is",key)

