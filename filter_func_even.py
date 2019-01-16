# TODO :a program which can filter even numbers in a list by using filter function


c = []
def filter_func(a):
    print(a)
    for x in a:
       if x%2 == 0:
            c.append(x)
    print(c)




a = [1,2,3,4,5,6,7,8,9]
filter_func(a)

