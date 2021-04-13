n = int(input())

easiest = ("", 100, 100)

for i in range(n):
    inp = input().split(" ")
    avg = (int(inp[1]) + int(inp[2]) + int(inp[3]))/3
    if (avg < easiest[1]):
        easiest = (inp[0], avg, int(inp[1]))
    elif (avg == easiest[1] and int(inp[1]) < easiest[2]):
        easiest = (inp[0], avg, int(inp[1]))

print(easiest[0])