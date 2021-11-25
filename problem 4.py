#Idris Adeyemi
#11/14/21
#problem 4, use the numbers in the list to write a code that comes back with a new unique element from the first list


def list(l):
    r = []
    for i in l:
        r.append(i)
    return r

x = [1,3,3,3,6,2,3,5]
print(list(x))
