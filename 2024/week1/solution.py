"""
Solution for Copying Hero
Created by Amy on 28th Feb
"""
import time

"""
Using selection sort (Time complexity O(n^2)) to sort the element
"""
def selection_sort(n: list):
    for i in range(len(n)-1):  # loop through the list
        min_element = n[i]
        min_pos = i
        for j in range(i, len(n)):  # loop through the list from position i
            if min_element > n[j]:  # if the current element is greater than the recorded max element, update
                min_element = n[j]
                min_pos = j
        n[i], n[min_pos] = n[min_pos], n[i]
    return n

def solution_selection_sort(input: str):
    start, stop, array = input.split('\n')
    start, stop = int(start), int(stop)
    array = [int(x) for x in array.split(' ')]  # numbers are space-separated
    sorted_array = selection_sort(array)
    answer = 0
    for index, number in enumerate(range(start, stop+1)):
        answer += abs(sorted_array[index] - number)
    return answer


"""
Merge Sort algorithm yoinked from https://www.geeksforgeeks.org/merge-sort/ because I am too tired to make one
"""
def merge_sort(n: list):
    if len(n) > 1:
        mid = len(n)//2
        left = n[:mid]
        right = n[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                n[k] = left[i]
                i += 1
            else:
                n[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            n[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            n[k] = right[j]
            k += 1
            j += 1

def solution_merge_sort(input: str):
    start, stop, array = input.split('\n')
    start, stop = int(start), int(stop)
    array = [int(x) for x in array.split(' ')]  # numbers are space-separated
    merge_sort(array)
    answer = 0
    for index, number in enumerate(range(start, stop+1)):
        answer += abs(array[index] - number)
    return answer

def solution_inbuilt_sort(input: str):
    start, stop, array = input.split('\n')
    start, stop = int(start), int(stop)
    array = [int(x) for x in array.split(' ')]  # numbers are space-separated
    array.sort()
    answer = 0
    for index, number in enumerate(range(start, stop+1)):
        answer += abs(array[index] - number)
    return answer


with open("test3.txt", "r") as file:
    text = file.read()
    result = None

    t0 = time.time()

    for _ in range(50):
        result = solution_merge_sort(text)
    print("Answer: ",result)
    print(f"Merge sort took {(time.time()-t0)/50} seconds (average of 50 runs)")

    t0 = time.time()

    print("Answer: ", solution_selection_sort(text))
    print(f"Selection sort took {(time.time() - t0)} seconds (1 run)")

    t0 = time.time()

    for _ in range(50):
        result = solution_inbuilt_sort(text)
    print("Answer: ", result)
    print(f"Inbuilt python sort took {(time.time()-t0)/50} seconds (average of 50 runs)")




