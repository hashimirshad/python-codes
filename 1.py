"""
input=1 2 3 4 5
output=10 14
"""

s = input()


def diagonalDifference():
    if s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:-2]
    elif s[-2:] == "AM":
        return s[:-2]
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    else:
        ans = int(s[:2]) + 12
        return str(str(ans) + s[2:8])


result = diagonalDifference()
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
