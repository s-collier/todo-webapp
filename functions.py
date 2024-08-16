FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):  # params of function
    """
    opens file containing todoitems
    :param filepath: filepath to file of todoitems
    :return: todos_local: list of todoitems
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# print the doc string for function get_todos
#print(help(get_todos))


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file
    :param todos_arg: the list of todoitems to write out
    :type todos_arg: list
    :param filepath: the filepath of file to write too
    :type filepath: string
    :return:
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

# __name__ is hidden variable with value __name__ a string
# when run cli.py then __name__ becomes functions

# allows execution when run file run directly cf via main
if __name__ == "__main__":
    print("Hello")
    print(get_todos())