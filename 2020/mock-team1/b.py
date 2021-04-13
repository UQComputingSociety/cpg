def upper_to_num(n):
    return ord(n) - ord('A') + 1

def lower_to_num(n):
    return ord(n) - ord('a') + 1

pin = input()
pattern = input()
pointer = 0

output_str = ""

try:
    for i in range(len(pattern)):
        if pattern[i].isupper():
            pointer += upper_to_num(pattern[i])
        else:
            for j in range(int(lower_to_num(pattern[i]))):
                output_str += pin[pointer]
                pointer += 1

    if pointer != len(pin):
        print("non sequitur")
    else:
        print(sum([int(i) for i in output_str]))
except IndexError:
    print("non sequitur")