result = []
while 1:
    try:
        num_people = int(input())
        networth = {p: 0 for p in (input().split(" "))}
        for i in range(num_people):
            y = input().split(" ")
            name, amount, num_rec = y[0], int(y[1]), int(y[2])
            if num_rec == 0:
                continue
            networth[name] = networth[name] - num_rec * (amount // num_rec)
            for people in y[3:]:
                networth[people] = networth[people] + (amount // num_rec)
        result.append("\n".join([f"{i} {networth[i]}" for i in networth]))
    except EOFError:
        break
print("\n\n".join(result))
