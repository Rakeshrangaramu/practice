# TODO : program to find a word in a dictionary.

a = {1 : "hi" , 2 : "every" , 3 : "one"}
print(a)
r = input("enter the word to be searched: ")
for element in a:
    s = a.get(element)
    if r == s:
        print("True")
#    break
    else:
        print("False")

