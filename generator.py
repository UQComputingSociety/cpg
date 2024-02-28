
import random
with open("test4.txt", 'w') as f:
    start = random.randint(10, 1000)
    f.write(str(start))
    f.write('\n')
    stop = random.randint(start, 100000)
    f.write(str(stop))
    f.write('\n')
    number_list = []
    for i in range(start, stop+1):
        number = random.randint(0, 10000000)
        number_list.append(str(number))
    f.write(' '.join(number_list))