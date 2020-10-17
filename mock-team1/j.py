from math import gcd

total, num_types = [int(x) for x in input().split()]

fractions = []
for i in range(num_types):
    fractions.append([int(x) for x in input().split()])

lcm = fractions[0][1]
for n, d in fractions:
    lcm = lcm * d // gcd(lcm, d)

# print(fractions)
# print(lcm)

coins = []
for n, d in fractions:
    coins.append(n * lcm // d)

total *= lcm

# print(coins)

from functools import lru_cache

inf = float('inf')

@lru_cache(maxsize=None)
def solve(i, total):
    if i >= num_types:
        return 0 if total == 0 else inf

    m = inf 
    value = coins[i]
    for x in range(0, total + 1, value):
        y = solve(i + 1, total - x) + x // value 
        if y < m:
            m = y
    return m 

sol = solve(0, total)
print(sol if sol != inf else '-1')