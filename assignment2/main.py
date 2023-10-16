
import random

def my_list(value: int) -> list:
    """
    :param value: this will be the length that the user will be able to choose
    :return: nothing, we will print the list
    """
    random_list = []
    for i in range(value):
        random_list.append(random.randint(0, 101))
    return random_list


def first_algorithm_cocktail_sort(array: list) -> list:
    """
    :param array: it will be given by my_list(number)
    :return: it will return the sorted list
    """
    changed = True
    start = 0
    end = len(array) - 1
    while changed:
        changed = False
        for i in range(start, end):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                changed = True
        if not changed:
            break
        end -= 1
        changed = False
        for i in range(end, start - 1, -1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                changed = True
        start += 1
        return array

def second_algorithm_heap_sort(array: list) -> list:
    def swap(array: list, i: int, j: int) -> None:
        array[i], array[j] = array[j], array[i]

    def heapify(array: list, i: int, upper: int) -> None:
        """
        :param array: it will be given by my_list(number)
        :param i: aka the parent
        :param upper: the upper bound of the list, it can be between 0 and len(array)
        :return: nothing will be returned
        """
        while True:
            left_child = 2*i + 1
            right_child = 2*i + 2
            if max(left_child, right_child) < upper:
                if array[i] >= max(array[left_child], array[right_child]): break
                elif array[left_child] > array[right_child]:
                    swap(array, i, left_child)
                    i = left_child
                else:
                    swap(array, i, right_child)
                    i = right_child
            elif left_child < upper:
                if array[left_child] > array[i]:
                    swap(array, i, left_child)
                    i = left_child
                else: break
            elif right_child < upper:
                if array[right_child] > array[i]:
                    swap(array, i, right_child)
                    i = right_child
                else: break
            else: break


    for i in range((len(array)-2)//2, -1, -1):
        heapify(array, i, len(array))
    for end in range(len(array)-1, 0, -1):
        swap(array, 0, end)
        heapify(array, 0, end)

    return(array)


if __name__ == "__main__":
    while True:
        problem = input("Which problem do you want to run?(1/2/3 or 4/x, if you want to exit)")
        if problem == '4' or problem == 'x':
            break

        number = int(input("Enter a number: "))

        if problem == '1':
            print(my_list(number))

        if problem == '2':
            print("The list is: ")
            value = my_list(number)
            print(value)
            print("Sorted list: ")
            print(first_algorithm_cocktail_sort(value))

        if problem == '3':
            print("The list is:")
            value = my_list(number)
            print(value)
            print("Sorted list:")
            print(second_algorithm_heap_sort(value))
