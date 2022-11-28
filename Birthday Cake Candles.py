"""input=4
input=3 2 1 3
output=2"""
n = int(input())
ar = list(map(int, input().split()[:n]))


def diagonalDifference(ar):
    c = 0
    temp = ar[0]
    for i in range(1, len(ar)):
        if ar[i] > temp:
            temp = ar[i]
    for i in range(0, len(ar)):
        if ar[i] == temp:
            c = c + 1
    return c


result = diagonalDifference(ar)
print(result)


""""exeeded time limit"""
# n = int(input())
# ar = list(map(int, input().split()[:n]))


# def diagonalDifference(ar):
#     c = 0
#     for i in range(0, len(ar)):
#         ar.sort()

#         a = ar[n - 1]
#         if ar[i] == a:
#             c = c + 1
#         else:
#             pass
#     print(c)


# diagonalDifference(ar)
