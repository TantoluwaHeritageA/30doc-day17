from math import factorial


def pascal(rows):
    print("Triangle: ")
    for i in range(0, rows):
        for j in range(rows - i + 1):
            print(end=' ')
        for k in range(0, i + 1):
            print(factorial(i)//(factorial(k) * factorial(i - k)), end=' ')
        print()


rows = int(input("Enter Number of Rows:  "))
pascal(rows)
