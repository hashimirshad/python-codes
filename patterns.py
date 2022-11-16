# *
# * *
# * * *
# * * * *
# * * * * *
def pattern(n):
    for i in range(0, n):

        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


n = 5
pattern(n)

# * * * * *
# * * * *
# * * *
# * *
# *
def pattern(n):
    for i in range(0, n):

        for j in range(0, n - i):
            print("* ", end="")
        print("\r")


n = 5
pattern(n)

# using list
def pypart(n):
    myList = []
    for i in range(1, n + 1):
        myList.append("*" * i)
    print("\n".join(myList))


# Driver Code
n = 5
pypart(n)
