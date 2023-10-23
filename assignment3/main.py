import random
import time

def my_random_list(value: int) -> list:
    """
    :param value: length of the list that will be generated
    :return: a list of random integers of length value
    """
    random_list = []
    for i in range(value):
        random_list.append(random.randint(0, 101))
    return random_list


def cocktail_sort(array: list) -> list:
    """
    :param array: list to be sorted
    :param step: the partially sorted list is displayed after step operation steps
    :return: the sorted list
    """
    changed = True
    start = 0
    end = len(array) - 1
    iteration = 0
    while changed:
        changed = False
        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                changed = True
                iteration += 1
        if not changed:
            break
        end -= 1
        changed = False
        for i in range(end, start - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                changed = True
                iteration += 1
        start += 1
    return array


def swap(array: list, i: int, j: int) -> None:
    array[i], array[j] = array[j], array[i]

def heapify(array: list, start: int, end: int) -> None:
    """
    :param array: the list
    :param start: aka the parent
    :param end: the upper bound of the list, it can be between 0 and len(array)
    :return: nothing will be returned
    """
    while True:
        left_child = 2 * start + 1
        right_child = 2 * start + 2
        if right_child < end:
            if array[start] >= max(array[left_child], array[right_child]):
                break
            elif array[left_child] > array[right_child]:
                swap(array, start, left_child)
                start = left_child
            else:
                swap(array, start, right_child)
                start = right_child
        elif left_child < end:
            if array[left_child] > array[start]:
                swap(array, start, left_child)
                start = left_child
            else:
                break
        elif right_child < end:
            if array[right_child] > array[start]:
                swap(array, start, right_child)
                start = right_child
            else:
                break
        else:
            break

def heap_sort(array: list) -> list:
    """
    :param array: list to be sorted
    :param step: the partially sorted list is displayed after step operation steps
    :return: the sorted list
    """
    iteration = 0
    for i in range((len(array) - 2) // 2, -1, -1):
        heapify(array, i, len(array))
        iteration += 1
    for end in range(len(array) - 1, 0, -1):
        swap(array, 0, end)
        heapify(array, 0, end)
        iteration += 1

    return (array)

def make_heap(array):
    for i in range((len(array) - 2) // 2, -1, -1):
        heapify(array, i, len(array))
    return array

test_cases = {
    'best': {
        'cocktail': [
            [i for i in range(1000)],
            [i for i in range(2000)],
            [i for i in range(4000)],
            [i for i in range(8000)],
            [i for i in range(16000)]
            #O(n)
        ],
        'heap': [
            make_heap([i for i in range(1000)]),
            make_heap([i for i in range(2000)]),
            make_heap([i for i in range(4000)]),
            make_heap([i for i in range(8000)]),
            make_heap([i for i in range(16000)])
            #O(nlogn)
        ]
    },
    'average': {
        'cocktail': [
            my_random_list(1000),
            my_random_list(2000),
            my_random_list(4000),
            my_random_list(8000),
            my_random_list(16000)
            #O(n^2)
        ],
        'heap': [
            my_random_list(1000),
            my_random_list(2000),
            my_random_list(4000),
            my_random_list(8000),
            my_random_list(16000)
            #O(n^2)
        ]
    },
    'worst': {
        'cocktail': [
            [i for i in range(1000, 0, -1)],
            [i for i in range(2000, 0, -1)],
            [i for i in range(4000, 0, -1)],
            [i for i in range(8000, 0, -1)],
            [i for i in range(16000, 0, -1)]
            #O(n*logn)
        ],
        'heap': [
            [i for i in range(1000, 0, -1)],
            [i for i in range(2000, 0, -1)],
            [i for i in range(4000, 0, -1)],
            [i for i in range(8000, 0, -1)],
            [i for i in range(16000, 0, -1)]
            #O(n^2)
        ]
    }
}

if __name__ == "__main__":
    test_case = test_cases["best"]

    while True:
        problem = input("What do you want to run?\n"
                        "1. Cocktail sort\n"
                        "2. Heap sort\n"
                        "3. Set best case\n"
                        "4. Set average case\n"
                        "5. Set worst case\n"
                        "6/x. Exit\n")
        if problem == '6' or problem == 'x':
            break

        if problem == '1':
            for array in test_case["cocktail"]:
                start = time.time()
                cocktail_sort(array)
                end = time.time()
                running_time = end - start
                print(f"for list of length {len(array)} running time is {running_time}" )

        if problem == '2':
            for array in test_case["heap"]:
                start = time.time()
                heap_sort(array)
                end = time.time()
                running_time = end - start
                print(f"for list of length {len(array)} running time is {running_time}" )

        if problem == '3':
            test_case = test_cases["best"]
        if problem == '4':
            test_case = test_cases["average"]
        if problem == '5':
            test_case = test_cases['worst']
