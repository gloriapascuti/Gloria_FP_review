import random
import math
import copy


def set_new_list(list_of_steps, the_list):
    list_of_steps.append(the_list)


def set_new_number(the_list: list, real: int, imaginary: int):
    complex_number_coordonates = []
    complex_number_coordonates.append(real)
    complex_number_coordonates.append(imaginary)
    the_list.append(complex_number_coordonates)


def initial_list():
    the_list = []
    for i in range(10):
        real = random.randint(1, 21)
        imaginary = random.randint(0, 20)
        set_new_number(the_list, real, imaginary)
    return the_list


def create_complex_number(string: str):
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
            imaginary = float(string[plus_index + 1:imaginary_index].strip())
        elif minus_index != -1:
            imaginary = float(string[minus_index + 1:imaginary_index].strip()) * (-1)
    else:
        imaginary = 0

    # return {"real": int(real), "imaginary": int(imaginary)}
    return [int(real), int(imaginary)]


def get_real(complex):
    return complex[0]


def get_imaginary(complex):
    if len(complex) < 2:
        return 0
    return complex[1]


def get_element(the_list, index):
    return the_list[index]


def print_complex(complex_list: list) -> str:
    result = ""
    for index in range(0, len(complex_list)):
        if index == len(complex_list) - 1:
            result = result + str(convert_to_string(complex_list[index]))
            break
        result = result + str(convert_to_string(complex_list[index])) + ', '
    return result


def convert_to_string(complex):
    if get_imaginary(complex) < 0:
        return f"{get_real(complex)} {get_imaginary(complex)}i"
    elif get_imaginary(complex) == 0:
        return f"{get_real(complex)}"
    return f"{get_real(complex)} + {get_imaginary(complex)}i"


def transform_list(input_string: str) -> list:
    # input_string = read_complex()
    lst = input_string.split(',')
    # print(lst)
    new_list = []
    correct_list = []
    for item in lst:
        new_list.append(item.strip())
    for number in new_list:
        correct_list.append(create_complex_number(number))
    return correct_list


# A -- ADD A NUMBER

def add_number_to_list(list_of_complex, number_as_a_string):
    number = create_complex_number(number_as_a_string)
    list_of_complex.append(number)


def insert_number_to_given_position(list_of_complex: list, number_as_a_string, position):
    number = create_complex_number(number_as_a_string)
    if position > len(list_of_complex) - 1:
        raise ValueError("invalid position!")
    list_of_complex.insert(position, number)


# B -- MODIFY NUMBERS

def remove_the_number_at_given_position(list_of_complex, position):
    if position > len(list_of_complex) - 1:
        raise ValueError("invalid position!")

    list_of_complex.pop(position)


def remove_the_numbers_at_given_start_to_end_position(list_of_complex, start_position, end_position):
    errors = ""
    if start_position < 0 or start_position > len(list_of_complex) - 1:
        errors += "invalid start position!\n"
    if end_position > len(list_of_complex) - 1:
        errors += "invalid end position!"
    if len(errors) > 0:
        raise ValueError(errors)

    del list_of_complex[start_position: end_position + 1]


def replace_all_numbers_equal_to_old_number_with_new_number(list_of_complex, old_number_as_string,
                                                            new_number_as_string):
    old_number = create_complex_number(old_number_as_string)
    new_number = create_complex_number(new_number_as_string)
    # TODO: display a message in the UI if it doesnt exist such number as old number
    for index in range(0, len(list_of_complex)):
        if list_of_complex[index] == old_number:
            list_of_complex[index] = new_number


# C -- DISPLAY NUMBERS HAVING DIFFERENT PROPERTIES

# for displaying the list we will use print_complex


def display_real_numbers_from_given_start_to_end_position(list_of_complex, start_position, end_position):
    errors = ""
    if start_position < 0 or start_position > len(list_of_complex) - 1:
        errors += "invalid start position!\n"
    if end_position > len(list_of_complex) - 1:
        errors += "invalid end position!"
    if len(errors) > 0:
        raise ValueError(errors)

    result = ""
    for index in range(start_position, end_position + 1):
        complex = list_of_complex[index]
        if get_imaginary(complex) == 0:
            if index == end_position:
                result = result + f"{get_real(complex)}"
                break
            result = result + f"{get_real(complex)}" + ', '
    result = result[:len(result) - 2]
    return result


def modulo_of_a_complex_number(complex_number):
    return math.sqrt((get_real(complex_number) ** 2) + (get_imaginary(complex_number)) ** 2)


def display_all_numbers_with_modulo_greater_than_given_value(list_of_complex, value):
    result = ""
    for complex in list_of_complex:
        if modulo_of_a_complex_number(complex) > value:
            result = result + convert_to_string(complex) + ', '
    result = result[:len(result) - 2]
    return result


def display_all_numbers_with_modulo_less_than_given_value(list_of_complex, value):
    result = ""
    for complex in list_of_complex:
        if modulo_of_a_complex_number(complex) < value:
            result = result + convert_to_string(complex) + ', '
    result = result[:len(result) - 2]
    return result


def display_all_numbers_with_modulo_greater_or_equal_than_given_value(list_of_complex, value):
    result = ""
    for complex in list_of_complex:
        if modulo_of_a_complex_number(complex) >= value:
            result = result + convert_to_string(complex) + ', '
    result = result[:len(result) - 2]
    return result


def display_all_numbers_with_modulo_less_or_equal_than_given_value(list_of_complex, value):
    result = ""
    for complex in list_of_complex:
        if modulo_of_a_complex_number(complex) <= value:
            result = result + convert_to_string(complex) + ', '
    result = result[:len(result) - 2]
    return result


def display_all_numbers_with_modulo_equal_to_given_value(list_of_complex, value):
    result = ""
    for complex in list_of_complex:
        if modulo_of_a_complex_number(complex) == value:
            result = result + convert_to_string(complex) + ', '
    result = result[:len(result) - 2]
    return result


# D -- FILTER THE LIST

def keep_only_real_numbers(list_of_complex):
    # TODO: display a message in the UI section is we dont have such numbers
    filter_list = []
    for index in range(0, len(list_of_complex)):
        complex = list_of_complex[index]
        if get_imaginary(complex) == 0:
            filter_list.append(list_of_complex[index])
    list_of_complex = filter_list
    return list_of_complex


def keep_only_numbers_with_modulo_less_than_given_value(list_of_complex, value):
    filter_list = []
    for complex in list_of_complex:
        if modulo_of_a_complex_number(complex) < value:
            filter_list.append(complex)
    list_of_complex = filter_list
    return list_of_complex


def keep_only_numbers_with_modulo_less_or_equal_than_given_value(list_of_complex, value):
    filter_list = []
    for complex in list_of_complex:
        if modulo_of_a_complex_number(complex) <= value:
            filter_list.append(complex)
    list_of_complex = filter_list
    return list_of_complex


def keep_only_numbers_with_modulo_greater_than_given_value(list_of_complex, value):
    filter_list = []
    for complex in list_of_complex:
        if modulo_of_a_complex_number(complex) > value:
            filter_list.append(complex)
    list_of_complex = filter_list
    return list_of_complex


def keep_only_numbers_with_modulo_greater_or_equal_than_given_value(list_of_complex, value):
    filter_list = []
    for complex in list_of_complex:
        if modulo_of_a_complex_number(complex) >= value:
            filter_list.append(complex)
    list_of_complex = filter_list
    return list_of_complex


def keep_only_numbers_with_modulo_equal_to_given_value(list_of_complex, value):
    filter_list = []
    for complex in list_of_complex:
        if modulo_of_a_complex_number(complex) == value:
            filter_list.append(complex)
    list_of_complex = filter_list
    return list_of_complex


# E -- UNDO


def add_to_list_of_steps_for_undo(the_list, list_of_steps_for_undo):
    '''
    funtion that appends the_list to list_of_steps_for_undo
    input: the_list - list of complex numbers, list_of_steps_for_undo - the list of privios states of the_list
    output: -
    '''
    new_list = copy.deepcopy(the_list)
    set_new_list(list_of_steps_for_undo, new_list)


def move_to_previous_state_of_the_list(list_of_steps_for_undo):
    list_of_steps_for_undo.pop()
    the_list = list_of_steps_for_undo[len(list_of_steps_for_undo) - 1]
    return the_list


def undo(the_list, list_of_steps_for_undo):
    the_list.clear()
    previous_list = move_to_previous_state_of_the_list(list_of_steps_for_undo)
    for index in range(0, len(previous_list)):
        set_new_number(the_list, get_real(get_element(previous_list, index)),
                       get_imaginary(get_element(previous_list, index)))
