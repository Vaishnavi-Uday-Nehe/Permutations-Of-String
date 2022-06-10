from itertools import permutations

def Mypermutations(str):

    MyList = permutations(str)

    for i in list (MyList):
        print(' '.join(i))

str = str(input("Enter Your String : "))
print(Mypermutations(str))