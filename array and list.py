# sum off 1d array
c = int(input())
m = list(map(int, input().split()[:c]))


sum = 0
for i in range(0, c):
    sum = sum + m[i]
print(sum)
