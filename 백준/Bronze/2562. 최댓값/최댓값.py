import sys
index =0
maxi = 0
for i in range(1,10):
    a = int(input())
    if a>= maxi:
        index =i
        maxi = a
print(maxi)
print(index)

