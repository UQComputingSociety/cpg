def helper(x: str):
    return sum([int(i) for i in x])

while 1:
    x = input()
    if x == '0':
        break
    while(len(x) != 1):
        x = str(helper(x))
    print(x)
