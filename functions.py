def get_todos(filepath):
    """Reads the file specified as argument and returns an array of todos, with each line in file (whitespace stripped) as a separate element"""
    with open(filepath, 'r') as todofile:
        tdl = [i.strip() for i in todofile.readlines()]
    return tdl
    

def put_todos(todolist, filepath):
    """Takes an array and writes each element to file after adding newline character so that each array element is written on a separate line"""
    writable = [i+'\n' for i in todolist]
    with open(filepath, 'w') as todofile:
        todofile.writelines(writable)