# TODO : program to find a word in a dictionary.

a = {1 : "hi" , 2 : "every" , 3 : "one"}
#print(a)
r = input("enter the word to be searched: ")
c = a.values()
#print(c)
if r in c:
    print("true")
else:
    print("false")
