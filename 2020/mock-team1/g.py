from math import ceil

m, n = [int(i) for i in input().split()]

total = 0
for i in range(m):
    total += int(input())

print(ceil(total / n))