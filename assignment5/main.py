# -----------------
# the non-UI functions
# -----------------

import math

def create_number(string: str) -> list:
    plus_index = string.find('+')
    minus_index = string.find('-')
    imaginary_index = string.find('i')

    if plus_index != -1:
        real = float(string[:plus_index].strip())
    elif minus_index != -1:
        real = float(string[:minus_index].strip())
    else:
        real = float(string.strip())

    if imaginary_index != -1:
        if plus_index != -1:
            imaginary = float(string[plus_index+1:imaginary_index].strip())
        elif minus_index != -1:
            imaginary = float(string[minus_index+1:imaginary_index].strip()) * (-1)
    else:
        imaginary = 0

    return [int(real), int(imaginary)]

def get_real(complex: list) -> str:
    return complex[0]

def get_imaginary(complex: list) -> str:
    return complex[1]

def print_complex(complex_list: list) -> str:
    result = ""
    for complex in complex_list:
        if complex == complex_list[-1]:
            result = result + str(convert_to_string(complex))
            break
        result = result + str(convert_to_string(complex)) + ', '
    return result

def convert_to_string(lst: list):
    if get_imaginary(lst) < 0:
        return f"{lst[0]} {lst[1]}i"
    return f"{lst[0]} + {lst[1]}i"




''''# def convert_from_dictionary_to_string(dict):
#     if dict['imaginary'] < 0:
#         return f"{dict['real']} {dict['imaginary']}i"
#     return f"{dict['real']} + {dict['imaginary']}i"
# 
# def print_complex(complex_list: list) -> str:
#     result = ""
#     for complex in complex_list:
#         if complex == complex_list[-1]:
#             result = result + str(convert_from_dictionary_to_string(complex))
#             break
#         result = result + str(convert_from_dictionary_to_string(complex)) + ', '
#     return result'''


# def create_number(string: str) :
#     plus_index = string.find('+')
#     minus_index = string.find('-')
#     imaginary_index = string.find('i')
#
#     if plus_index != -1:
#         real = float(string[:plus_index].strip())
#     elif minus_index != -1:
#         real = float(string[:minus_index].strip())
#     else:
#         real = float(string.strip())
#
#     if imaginary_index != -1:
#         if plus_index != -1:
#             imaginary = float(string[plus_index+1:imaginary_index].strip())
#         elif minus_index != -1:
#             imaginary = float(string[minus_index+1:imaginary_index].strip()) * (-1)
#     else:
#         imaginary = 0
#
#     return {"real": int(real), "imaginary": int(imaginary)}
#
# def get_real(complex) :
#     return complex["real"]
#
# def get_imaginary(complex) :
#     return complex["imaginary"]
#
# def print_complex(complex_list: list) -> str:
#     result = ""
#     for complex in complex_list:
#         if complex == complex_list[-1]:
#             result = result + str(convert_to_string(complex))
#             break
#         result = result + str(convert_to_string(complex)) + ', '
#     return result
#
# def convert_to_string(complex):
#     if get_imaginary(complex) < 0:
#         return f"{get_real(complex)} {get_imaginary(complex)}i"
#     return f"{get_real(complex)} + {get_imaginary(complex)}i"

def transform_list(input_string: str) -> list:
    # input_string = read_complex()
    lst = input_string.split(',')
    # print(lst)
    new_list = []
    correct_list = []
    for item in lst:
        new_list.append(item.strip())
    for number in new_list:
        correct_list.append(create_number(number))
    return correct_list


def are_equal(complex_number_1, complex_number_2) -> bool:
    if get_real(complex_number_1) == get_real(complex_number_2) and get_imaginary(complex_number_1) == get_imaginary(complex_number_2):
        return True
    return False

def absolute_value_of_a_complex_number(complex_number):
    return math.sqrt((get_real(complex_number) ** 2) + (get_imaginary(complex_number)) ** 2)


## PROBLEM FROM 3A
def in_dict(complex_number, dictionary):
    return convert_to_string(complex_number) in dictionary

def add_complex_to_dict(complex_number, dictionary, value):
    dictionary[convert_to_string(complex_number)] = value

def get_value_from_dict(complex_number, dictionary):
    return dictionary[convert_to_string(complex_number)]

def longest_subarray_of_distinct_numbers(list_of_complex_numbers):
    length = len(list_of_complex_numbers)
    start = 0
    end = 0
    max_length = 0
    max_subarray = []
    last_index = {}

    while end < length:
        if not in_dict(list_of_complex_numbers[end], last_index) or get_value_from_dict(list_of_complex_numbers[end], last_index) < start:
            # last_index[list_of_complex_numbers[end]] = end
            add_complex_to_dict(list_of_complex_numbers[end], last_index, end)
            end = end+1
            current_length = end - start
            if current_length > max_length:
                max_length = current_length
                max_subarray = list_of_complex_numbers[start:end]
        else:
            # start = last_index[list_of_complex_numbers[end]]+1
            start = get_value_from_dict(list_of_complex_numbers[end], last_index) + 1

    return max_length, max_subarray

## PROBLEM FROM 3B

def longest_alternating_sequence(nums):
    n = len(nums)
    if n < 2:
        return n

    # Initialize variables to keep track of the length of the longest
    # wiggle subsequence and the last wiggle direction
    max_len = 1
    last_wiggle = None

    for i in range(1, n):
        # Calculate the difference between the current and previous element
        diff = absolute_value_of_a_complex_number(nums[i]) - absolute_value_of_a_complex_number(nums[i - 1])
        # If the difference is positive and the last wiggle direction was negative
        # or the difference is negative and the last wiggle direction was positive,
        # then we've found a new wiggle direction and can update the length of the
        # longest wiggle subsequence
        if (diff > 0 and last_wiggle != 1) or (diff < 0 and last_wiggle != -1):
            max_len += 1
            # Update the last wiggle direction
            last_wiggle = 1 if diff > 0 else -1

    return max_len


# def main():
#     #my_list = []
#     example_input_string = "2 + 3i, 2 + 3i, 2 + 4i, 1 + 3i, 5 + 13i, 2 + 3i, 5 - 4i, 7 - 3i"
#     example_input_string = "1 + 1i, 17 + 17i, 5 + 5i, 10 + 10i, 13 + 13i, 15 + 15i, 10 + 10i, 5 + 5i, 16 + 16i, 8 + 8i"
#     #input_complex_numbers = input("Chose the length of the list: ")
#     #print(read_list(example_input_string))
#     #length = int(input("Chose the length of the list: "))
#     #print(read_list(length))
#     # input_str = read_complex()
#     # print(input_str)
#     #list_of_complex_numbers = input("Enter your list of complex numbers:")
#     my_list = transform_list(example_input_string)
#     print(my_list)
#     print(print_complex(my_list))
#     print()
#     length, subarray = longest_subarray_of_distinct_numbers(my_list)
#     print(length)
#     print(subarray)
#     print(longest_alternating_sequence(my_list))
#
#     # print(print_complex(subarray))
#     # lst = create_number('2   + 3i')
#     # print(lst)
#     # print(help(str))

# -----------------
# the UI functions
# -----------------


def longest_subarray_of_distinct_numbers_ui(lst):
    length, subarray = longest_subarray_of_distinct_numbers(lst)
    print("The length of the longest subarray is: ", length)
    print("The subarray is: ", print_complex(subarray), '\n')


def longest_alternating_sequence_ui(lst):
    length = longest_alternating_sequence(lst)
    print("The length of the longest alternating sequence is: ", length)



def print_menu():
    print("\t Problems with complex numbers \n"
          "1. Read a list of complex number with the format: a+bi \n"
          "2. Display the list of complex numbers \n"
          "3. A. Find and display the length and elements of a longest subarray of distinct numbers. \n"
          "3. B. Find and display the length of a longest alternating subsequence, when considering each number's modulus "
          "(e.g., given sequence [1, 3, 2, 4, 10, 6, 1], [1, 3, 2, 10] is an alternating subsequence, because 1 < 3 > 2 < 10) \n"
          "4. Exit")

# print_menu()

def start():
    """
     1. Print  the menu
     2. Read option
     3. Compute the problem chosen
    """
    example_input_string = "1 + 1i, 17 + 17i, 5 + 5i, 10 + 10i, 13 + 13i, 15 + 15i, 10 + 10i, 5 + 5i, 16 + 16i, 8 + 8i"
    my_list = []
    empty_list = True
    while True:
        print_menu()
        option = input(">>>")
        if option == "1":
            list_of_complex_numbers =  input("Enter your list of complex numbers:")
            my_list = transform_list(list_of_complex_numbers)
            empty_list = False
        elif option == "2":
            if empty_list:
                print(example_input_string)
            else:
                print(print_complex(my_list))
                # print(my_list)
        elif option == "3":
            option_3 = input("Please chose between option a or b: ")
            if option_3 == "a":
                if empty_list:
                    print(longest_subarray_of_distinct_numbers_ui(transform_list(example_input_string)))

                else:
                    print(longest_subarray_of_distinct_numbers_ui(my_list))
            elif option_3 == "b":
                if empty_list:
                    print(longest_alternating_sequence_ui(transform_list(example_input_string)))

                else:
                    print(longest_alternating_sequence_ui(my_list))
        elif option == "4" or option == "x":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    start()
    # main()