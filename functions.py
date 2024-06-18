import csv, glob

def get_todos(filepath):
    """Reads the file specified as argument and returns an array of todos, with each line in file (whitespace stripped) as a separate element"""
    try:
        with open(filepath, 'r') as todofile:
            if filepath.endswith('.txt'):
                tdl = [i.strip() for i in todofile.readlines()]
            elif filepath.endswith('.csv'):
                tdl = list(csv.DictReader(todofile))
            return tdl
    except FileNotFoundError:
        with open(filepath, 'w') as todofile:
            return []
    

def put_todos(todolist, filepath):
    """Takes an array and writes each element to file after adding newline character so that each array element is written on a separate line. Currently supports separate writing todos into - .txt"""
    if filepath.endswith('.txt'):
        writable = [i+'\n' for i in todolist]
        with open(filepath, 'w') as todofile:
            todofile.writelines(writable)
    elif filepath.endswith('.csv'):
        pass


def todo_show_csv(filepath):
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


def all_todo_files(*valid_extensions):
    """Takes a list of valid extensions (without the '.' symbol and returns a list of all files with that extension in the operating folder)"""
    valid_extensions = set(valid_extensions + ('txt', 'csv'))
    file_list = []
    for extension in valid_extensions:
        file_list += glob.glob('*.'+extension)
    return file_list