FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of to-do items. """
    with open(filepath, 'r') as file_local:  # Create a file With-Context Manager. With-Context Manager, you do not need
        todos_local = file_local.readlines()  # to close the file. It closes the file implicitly.
    return todos_local


def write_todos(todos_arg, filepath="todo.txt"):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
