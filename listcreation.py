ar = []
n = int(input())
for i in range(0, n):
    a = input()
    ar.append(a)
print(ar)


# using exept method..
# we can create list without mentioning the length
try:
    ar = []
    while True:
        ar.append(int(input()))
except:
    print(ar)
    print(len(ar))

# For list of integers
lst1 = []

# For list of strings/chars method 3
lst2 = []

lst1 = [int(item) for item in input("Enter the list items : ").split()]

lst2 = [item for item in input("Enter the list items : ").split()]

print(lst1)
print(lst2)
