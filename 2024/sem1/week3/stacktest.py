"""
I know this is bad practice but I don't have time to write unit test :'(
"""


def check_validity_of_answer(output_file: str, input_file: str):
    with open(output_file, 'r') as o:
        answers = o.read()
    with open(input_file, 'r') as i:
        testcases = i.read()
    answers = answers.split('\n')
    testcases = testcases.split('\n')[1:]
    valid = True
    for i, testcase in enumerate(testcases):
        answer = [int(x) for x in answers[i].split(' ')]
        length = len(testcase)  # number of letters in the given input
        if len(answer) != length + 1:
            print("Test failed, the number of integers in output should be 1 more than the number of letters in input")
            valid = False
            break
        for j, letter in enumerate(testcase):
            if (answer[j+1] > answer[j] and letter == "D") or (answer[j+1] < answer[j] and letter == "I"):
                print("Pattern does not match")
                valid = False
                break
        if len(set(answer)) != len(answer):
            valid = False
            print("Numbers are not unique")
        if min(answer) != 1 and max(answer) != length+1:
            valid = False
            print("The sequence is not minimal")
        if not valid:
            break
    if valid:
        print("Congratulations! Test passed")



