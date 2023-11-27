from functions import *


def commands_for_add_number(list_to_append, the_input_command_string):
    lst = the_input_command_string.split()
    if lst[0] == "add":
        add_number_to_list(list_to_append, lst[1])
    elif lst[0] == "insert" and lst[2] == "at":
        complex_number = lst[1]
        position = int(lst[3])
        insert_number_to_given_position(list_to_append, complex_number, position)
    else:
        raise ValueError("invalid command for adding an new number!")


def commands_for_modify_number(list_to_append, the_input_command_string):
    lst = the_input_command_string.split()
    if len(lst) == 4:
        if lst[0] == "remove" and lst[2] == "to":
            # start_position = int(lst[1].strip)
            # end_position = int(lst[3].strip)
            remove_the_numbers_at_given_start_to_end_position(list_to_append, int(lst[1]), int(lst[3]))
        elif lst[0] == "replace" and lst[2] == "with":
            old_number = lst[1]
            new_number = lst[3]
            replace_all_numbers_equal_to_old_number_with_new_number(list_to_append, old_number, new_number)
        else:
            raise ValueError("invalid command for modifying numbers!")
    elif len(lst) == 2:
        if lst[0] == "remove":
            position = int(lst[1])
            remove_the_number_at_given_position(list_to_append, position)
        else:
            raise ValueError("invalid command for modifying numbers!")
    elif len(lst) == 0:
        raise ValueError("invalid command for modifying numbers!")
    else:
        raise ValueError("invalid command for modifying numbers!")


def commands_for_displaying_numbers_based_on_properties(list_to_display, the_input_command_string):
    lst = the_input_command_string.split()
    if len(lst) == 1:
        if lst[0] == "list":
            print(print_complex(list_to_display))
    elif len(lst) == 5 and lst[0] == "list":
        if lst[1] == "real" and lst[3] == "to":
            print(display_real_numbers_from_given_start_to_end_position(list_to_display, int(lst[2]), int(lst[4])))
        else:
            raise ValueError("invalid command for displaying numbers based on properties!")
    elif len(lst) == 4 and lst[0] == "list" and lst[1] == "modulo":
        if lst[2] == "<":
            print(display_all_numbers_with_modulo_less_than_given_value(list_to_display, int(lst[3])))
        elif lst[2] == "<=":
            print(display_all_numbers_with_modulo_less_or_equal_than_given_value(list_to_display, int(lst[3])))
        elif lst[2] == ">":
            print(display_all_numbers_with_modulo_greater_than_given_value(list_to_display, int(lst[3])))
        elif lst[2] == ">=":
            print(display_all_numbers_with_modulo_greater_or_equal_than_given_value(list_to_display, int(lst[3])))
        elif lst[2] == "=":
            print(display_all_numbers_with_modulo_equal_to_given_value(list_to_display, int(lst[3])))
        else:
            raise ValueError("invalid command for displaying numbers based on properties!")
    elif len(lst) == 0:
        raise ValueError("invalid command for displaying numbers based on properties!")
    else:
        raise ValueError("invalid command for displaying numbers based on properties!")


def commands_for_filtering_the_list(list_to_keep, the_input_command_string):
    lst = the_input_command_string.split()
    if len(lst) == 2 and lst[0] == "filter" and lst[1] == "real":
        print(keep_only_real_numbers(list_to_keep))
    elif len(lst) == 4 and lst[0] == "filter" and lst[1] == "modulo":
        if lst[2] == "<":
            print(keep_only_numbers_with_modulo_less_than_given_value(list_to_keep, int(lst[3])))
        elif lst[2] == "<=":
            print(keep_only_numbers_with_modulo_less_or_equal_than_given_value(list_to_keep, int(lst[3])))
        elif lst[2] == ">":
            print(keep_only_numbers_with_modulo_greater_than_given_value(list_to_keep, int(lst[3])))
        elif lst[2] == ">=":
            print(keep_only_numbers_with_modulo_greater_or_equal_than_given_value(list_to_keep, int(lst[3])))
        elif lst[2] == "=":
            print(keep_only_numbers_with_modulo_equal_to_given_value(list_to_keep, int(lst[3])))
        else:
            raise ValueError("invalid command for filtering the list!")
    elif len(lst) == 0:
        raise ValueError("invalid command for filtering the list!")
    else:
        raise ValueError("invalid command for filtering the list!")


def undo_command(the_list, list_of_steps_for_undo):
    if len(list_of_steps_for_undo) == 0:
        raise ValueError("There are no commands to undo!")
    undo(the_list, list_of_steps_for_undo)


if __name__ == "__main__":
    listt = [[1, 2], [2, 0], [10, 0], [9, 9], [1, 2]]
    command = "filter modulo > 10"
    try:
        commands_for_filtering_the_list(listt, command)
    except ValueError as ve:
        print(ve)
    # print(listt)

    # string = "      add       a+bi"
    # lst = string.split()
    # print(lst)
