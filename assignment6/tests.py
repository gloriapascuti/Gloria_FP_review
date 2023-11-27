from functions import *
from commands import *


def test_insert_number_to_given_position():
    lst = [[1, 2], [2, 3], [3, 4]]
    try:
        insert_number_to_given_position(lst, "2+3i", 3)
        assert False
    except ValueError as ve:
        assert str(ve) == "invalid position!"


def test_remove_the_number_at_given_position():
    lst = [[1, 2], [2, 3], [3, 4]]
    try:
        remove_the_number_at_given_position(lst, 3)
        assert False
    except ValueError as ve:
        assert str(ve) == "invalid position!"


def test_remove_the_numbers_at_given_start_to_end_position():
    lst = [[1, 2], [2, 3], [3, 4]]
    try:
        remove_the_numbers_at_given_start_to_end_position(lst, -1, 3)
        assert False
    except ValueError as ve:
        assert str(ve) == "invalid start position!\ninvalid end position!"
        # print(ve)


def test_display_real_numbers_from_given_start_to_end_position():
    lst = [[1, 2], [2, 3], [3, 4]]
    try:
        remove_the_numbers_at_given_start_to_end_position(lst, -1, 3)
        assert False
    except ValueError as ve:
        assert str(ve) == "invalid start position!\ninvalid end position!"


def test_commands_for_add_number():
    lst = [[1, 2], [2, 3], [3, 4]]
    try:
        commands_for_add_number(lst, "asghu")
        assert False
    except ValueError as ve:
        assert str(ve) == "invalid command for adding an new number!"


def test_commands_for_modify_number():
    lst = [[1, 2], [2, 3], [3, 4]]
    try:
        commands_for_modify_number(lst, "asdgi")
        assert False
    except ValueError as ve:
        assert str(ve) == "invalid command for modifying numbers!"


def test_commands_for_displaying_numbers_based_on_properties():
    lst = [[1, 2], [2, 3], [3, 4]]
    try:
        commands_for_displaying_numbers_based_on_properties(lst, "")
        assert False
    except ValueError as ve:
        assert str(ve) == "invalid command for displaying numbers based on properties!"


def test_commands_for_filtering_the_list():
    lst = [[1, 2], [2, 3], [3, 4]]
    try:
        commands_for_filtering_the_list(lst, "")
        assert False
    except ValueError as ve:
        assert str(ve) == "invalid command for filtering the list!"


def test_add_to_list_of_steps_for_undo():
    lst = [[1, 2], [2, 3], [3, 4]]
    list_of_steps_for_undo = []
    add_to_list_of_steps_for_undo(lst, list_of_steps_for_undo)


def test_move_to_previous_state_of_the_list():
    lst = [[1, 2], [2, 3], [3, 4]]
    list_of_steps_for_undo = []
    add_to_list_of_steps_for_undo(lst, list_of_steps_for_undo)
    print(move_to_previous_state_of_the_list(lst, list_of_steps_for_undo))


def add_to_list_of_steps_for_undo__the_list__the_list_at_last_position():
    the_list = initial_list()
    list_of_steps_for_undo = []
    add_to_list_of_steps_for_undo(the_list, list_of_steps_for_undo)
    assert (list_of_steps_for_undo[len(list_of_steps_for_undo) - 1] == the_list)


def run_all_tests():
    test_insert_number_to_given_position()
    test_remove_the_number_at_given_position()
    test_remove_the_numbers_at_given_start_to_end_position()
    test_display_real_numbers_from_given_start_to_end_position()
    test_commands_for_add_number()
    test_commands_for_modify_number()
    test_commands_for_displaying_numbers_based_on_properties()
    test_commands_for_filtering_the_list()
    # test_add_to_list_of_steps_for_undo()
    # test_move_to_previous_state_of_the_list()
    # add_to_list_of_steps_for_undo__the_list__the_list_at_last_position()


if "__name__" == "__main__":
    run_all_tests()
    #
    listt = [[1, 2], [2, 0], [10, 0], [9, 9], [1, 2]]
    # add_number_to_list(listt, "2-3i")
    # print(display_real_numbers_from_given_start_to_end_position(listt, 0, 3))
    # print(listt)
    # print(keep_only_real_numbers(listt))
    # command = input(">>>")
