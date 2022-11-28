n = int(input())
m = list(map(int, input().split()[:n]))

sum = 0
a = len(m)
for i in range(n):
    sum = sum + m[i]

print(sum)
