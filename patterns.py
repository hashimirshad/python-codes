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

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
def pattern(n):
    k = n - 1
    # raw
    for i in range(0, n):
        # space
        for j in range(0, k):

            print(end=" ")
        k = k - 1
        # * printing
        for a in range(0, i + 1):
            print("* ", end="")
        print("\r")


n = 5
pattern(n)

#          *
#        * *
#      * * *
#    * * * *
#  * * * * *


def pattern(n):
    k = 2 * n - 1
    for i in range(0, n):

        for j in range(0, k):

            print(end=" ")
        k = k - 2
        for a in range(0, i + 1):
            print("* ", end="")
        print("\r")


n = 5
pattern(n)
#          1
#        1 2
#      1 2 3
#    1 2 3 4
#  1 2 3 4 5


def pattern(n):
    num = 1
    k = 2 * n - 1
    for i in range(0, n):
        num = 1
        for j in range(0, k):

            print(end=" ")
        k = k - 2
        for a in range(0, i + 1):
            print(num, end=" ")
            num = num + 1

        print("\r")


n = 5
pattern(n)
#          A
#        B C
#      D E F
#    G H I J
#  K L M N O
def pattern(n):
    num = 65
    k = 2 * n - 1
    for i in range(0, n):
        # num = 66
        for j in range(0, k):

            print(end=" ")
        k = k - 2
        for a in range(0, i + 1):
            ch = chr(num)
            print(ch, end=" ")
            num = num + 1

        print("\r")


n = 5
pattern(n)

# A
# B C
# D E F
# G H I J
# K L M N O


def pattern(n):
    num = 65
    k = n - 1
    for i in range(0, n):
        # # num = 66
        # for j in range(0, k):

        #     print(end=" ")
        # k = k - 1
        for a in range(0, i + 1):
            ch = chr(num)
            print(ch, end=" ")
            num = num + 1

        print("\r")


n = 5
pattern(n)
