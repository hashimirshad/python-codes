n = int(input())
arr = list(map(int, input().split()[:n]))


def diagonalDifference(arr):
    a, b, c = 0, 0, 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            a = a + 1
        elif arr[i] < 0:
            b = b + 1
        else:
            c = c + 1

    print(a / len(arr))
    print(b / len(arr))
    print(c / len(arr))


diagonalDifference(arr)
