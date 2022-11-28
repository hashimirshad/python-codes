"""reverse of numbers array
Split() function uses whitespace string as separator and removes the empty strings,strip() extra white spaces in the begining and ending"""
n = int(input())
m = input().strip().split(" ")
# [<start_index>, <stop_index>, <step>]
res = m[3:4:-1]
r = ""

for i in range(n):
    r = r + str(res[i]) + " "

print(r)

# m.reverse()
# for i in m:
#     print(i, end=" ")
