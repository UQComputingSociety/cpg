from collections import defaultdict

a, b = input().split()
if len(a) < len(b):
    pass
elif len(a) > len(b):
    a, b = b, a
else:
    a, b = sorted([a, b])

if a == b:
    print(a, "is identical to", b)
elif abs(len(a) - len(b)) > 1:
    print(a, "is nothing like", b)
else:
    al = defaultdict(lambda: 0)
    bl = defaultdict(lambda: 0)
    for l in a:
        if l in al:
            al[l] = al[l] + 1
        else:
            al[l] = 1
    for l in b:
        if l in bl:
            bl[l] = bl[l] + 1
        else:
            bl[l] = 1
    diff = 0
    diff_letters = []
    for k in set(al.keys()) | set(bl.keys()):
        # print(k, al[k], bl[k])
        d = abs(al[k] - bl[k])
        diff += d
        # print(diff)

        if d == 1:
            diff_letters.append(k)

    def check_almost():
        if len(diff_letters) != 2: return 0 
        c1, c2 = diff_letters 
        d1 = al[c1] - bl[c1]
        d2 = al[c2] - bl[c2]

        return (d1 == 1 and d2 == -1 or d1 == -1 and d2 == 1)

    # print(diff_letters)
    if check_almost():
        print(a, "is almost an anagram of", b)
    elif diff > 1:
        print(a, "is nothing like", b)
    elif diff == 1:
        print(a, "is almost an anagram of", b)
    else:
        print(a, "is an anagram of", b)