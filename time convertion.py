"""
24 to 12
07:05:45PM
19:05:45
"""
s = int(input())
d = int(input())


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
