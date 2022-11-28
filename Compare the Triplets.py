"""The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

If a[i] > b[i], then Alice is awarded 1 point.
If a[i] < b[i], then Bob is awarded 1 point.
If a[i] = b[i], then neither person receives a point."""
c = 3
m = list(map(int, input().split()[:c]))
n = list(map(int, input().split()[:c]))
a = 0
b = 0
for i in range(0, c):
    if m[i] > n[i]:
        a = a + 1
    elif m[i] < n[i]:
        b = b + 1
    else:
        pass
print(a, b)
