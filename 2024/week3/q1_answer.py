import math
import random


def decode(seq):
    stack = []
    result = []
    for i in range(len(seq) + 1):
        if i == len(seq) or seq[i] == "I":
            result.append(str(i + 1))
            while stack:  # When stack is not empty
                result.append(stack.pop())
        else:
            stack.append(str(i + 1))
    return ' '.join(result)


with open("out_example.txt", 'w') as text:
    outputs = []
    with open("testcases_q1_demo.txt", 'r') as inputs:
        inputs_text = inputs.read()
    for i in inputs_text.split('\n')[1:]:
        outputs.append(decode(i))
    text.write("\n".join(outputs))

#
# from stacktest import check_validity_of_answer
# check_validity_of_answer("out.txt", "testcases_q1.txt")
