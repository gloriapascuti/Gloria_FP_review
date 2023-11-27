from tests import *


def ui_read():
    input_data = input("Type in the command:")
    return input_data


def ui_print_menu():
    print("Commands:\n"
          "~ Add numbers to the list: \n"
          "add <number>\n"
          "insert <number> at <position>\n\n"
          "~ Modify elements from the list:\n"
          "remove <position>\n"
          "remove <start position> to <end position>\n"
          "replace <old number> with <new number>\n\n"
          "~ Display numbers having different properties:\n"
          "list\n"
          "list real <start position> to <end position>\n"
          "list modulo [ < | = | > ] <number>\n\n"
          "~ Filter the list:\n"
          "filter real\n"
          "filter modulo [ < | = | > ] <number>\n\n"
          "~ Undo\n")


def main():
    run_all_tests()
    the_list = initial_list()
    list_of_steps_for_undo = []
    add_to_list_of_steps_for_undo(the_list, list_of_steps_for_undo)
    ui_print_menu()
    commands = {
        'add': commands_for_add_number,
        'insert': commands_for_add_number,
        'remove': commands_for_modify_number,
        'replace': commands_for_modify_number,
        'list': commands_for_displaying_numbers_based_on_properties,
        'filter': commands_for_filtering_the_list,
    }
    while True:
        input_data = ui_read()
        command = input_data.split()[0]
        if 'exit' == command:
            return
        elif 'undo' == command:
            try:
                undo_command(the_list, list_of_steps_for_undo)
            except ValueError as ve:
                print(ve)
        elif command in commands:
            try:
                commands[command](the_list, input_data)
                if command != "list":
                    add_to_list_of_steps_for_undo(the_list, list_of_steps_for_undo)
            except ValueError as ve:
                print(ve)
        else:
            print("Invalid command!")


main()
