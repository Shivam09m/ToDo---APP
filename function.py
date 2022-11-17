FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read the file and returns list of ToDo items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the file with updated ToDo list"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
