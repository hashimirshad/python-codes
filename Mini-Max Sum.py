"""
input=1 2 3 4 5
output=10 14
"""
n = 5
arr = list(map(int, input().split()[:n]))


def diagonalDifference(arr):
    arr.sort()
    max = arr[1:]
    min = arr[:-1]
    print(sum(min), sum(max))


diagonalDifference(arr)
