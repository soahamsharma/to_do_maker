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

import csv
def todo_show(filepath):
    with open(filepath, 'r') as file:
        todos = csv.DictReader(file)
        counter = 1
        for item in todos:
            if int(item['edited']):
                operation = 'Last edited'
            else:
                operation = 'Added'
            print(counter, '.)', item['todo'], '---', operation ,' on', item['last_access_date'])
            counter += 1
