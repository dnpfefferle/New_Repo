listOne = [1, 2, 3, 4, 5, 6, 7]
listTwo = [10, 20, 30]

def listinformation(simplelist):
    print(f"The values in this list are...")
    for value in simplelist:
        print(value)
    print(f"The length of this list is..." + str(len(simplelist)))

listinformation(listOne)
listinformation(listTwo)
    