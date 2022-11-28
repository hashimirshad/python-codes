n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split()[:n])))


def diagonalDifference(arr):
    # Write your code here
    left_diag = [arr[i][i] for i in range(0, len(arr))]
    right_diag = [arr[i][~i] for i in range(0, len(arr))]
    a = abs(sum(left_diag) - sum(right_diag))
    print(left_diag)
    print(a)


diagonalDifference(arr)
