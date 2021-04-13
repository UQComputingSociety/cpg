num_types = int(input())

min1, max1 = [int(x) for x in input().split()]
min2, max2 = [int(x) for x in input().split()]

num_sushis = [int(input()) for x in range(num_types)]

#print(num_sushis)

from functools import lru_cache

@lru_cache(maxsize=None)
def sushis(i, num1, num2):
    if num1 > max1: return False
    if num2 > max2: return False 
    if i >= num_types:
        return num1 >= min1 and num2 >= min2

    n = num_sushis[i]
    half = n // 2
    if n % 2 == 0:
        return sushis(i + 1, num1 + half, num2 + half)
    else:
        return sushis(i + 1, num1 + half + 1, num2 + half) \
            or sushis(i + 1, num1 + half, num2 + half + 1)

print("Yes" if sushis(0, 0, 0) else "No")