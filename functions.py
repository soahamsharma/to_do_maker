import csv, glob


def plain_text_todo_parser(text_todo: str) -> dict:
    """Gets a todo as written in plaintext (default format only) in a text file and returns a todo object (currently implemented as dict)"""
    todo_elements =[i.strip() for i in text_todo.split('-')]
    last_access = todo_elements[1].split(' on ')
    edited = 1 if 'edited' in last_access[0].lower() else 0
    if len(todo_elements) == 3 and todo_elements[2].lower().startswith('due'):
        due_date = todo_elements[2].lower().replace('due on: ', '')
    else: 
        due_date = None
    todo_object = {'todo': todo_elements[0], 'access_date': last_access[1],'edited': edited, 'due': due_date}
    return todo_object

def plain_text_todo_writer(dict_todo: dict) -> str:
    """Gets a todo object (currently implemented as dict) and returns a line of plain text
    in the format '<todo_text> - (Added|Last Edited) on <last_access_date> - Due on <due_date>"""
    body_text = dict_todo['todo']
    access_messsage = (" - Last edited on " if dict_todo['edited'] else ' - Added on ') + dict_todo['access_date']
    due_message = (" - Due on: " + dict_todo['due']) if ('due' in dict_todo and dict_todo['due']) else ""
    return body_text + access_messsage + due_message


def get_todos(filepath: str) -> list:
    """Reads the file specified as argument and returns an array of todos, with each line in file (whitespace stripped) as a separate element"""
    try:
        with open(filepath, 'r') as todofile:
            if filepath.endswith('.txt'):
                tdl = [i.strip() for i in todofile.readlines()]
                tdl = [plain_text_todo_parser(i) for i in tdl]
            elif filepath.endswith('.csv'):
                tdl = list(csv.DictReader(todofile))
            return tdl
    except FileNotFoundError:
        print("File does not currently exist, creating new file")
        with open(filepath, 'w') as todofile:
            return []

def show_todos(filepath):
    toDo = get_todos(filepath)
    if len(toDo) == 0:
        print('to-do list currently empty.')
    for i, item in enumerate(toDo):
        print(f"{str(i+1)}) {plain_text_todo_writer(item)}")
    

def put_todos(todolist: list, filepath: str) -> None:
    """Takes an array and writes each element to file after adding newline character so that each array element is written on a separate line. Currently supports separate writing todos into - .txt"""
    if filepath.endswith('.txt'):
        writable = [plain_text_todo_writer(i) for i in todolist]
        with open(filepath, 'w') as todofile:
            todofile.writelines(writable)
    elif filepath.endswith('.csv'):
        with open(filepath, 'w') as todofile:
            writer = csv.DictWriter(todofile, fieldnames=todolist[0].keys())
            writer.writeheader()
            for i in todolist:
                writer.writerow(i)


def all_todo_files(valid_extensions: list) -> list:
    """Takes a list of valid extensions (without the '.' symbol and returns a list of all files with that extension in the operating folder)"""
    valid_extensions = set(valid_extensions + ['txt', 'csv'])
    file_list = []
    for extension in valid_extensions:
        file_list += glob.glob('*.'+extension)
    return file_list

def pretty_print_all_todo_files(working_file: str, extensions: list) -> None:
        print('Currently created todo lists - ')
        print('    ', *all_todo_files(extensions), sep=' | ', end=' | \n')
        print('     Active todo file - ' + working_file)
        print("to change active todo file, type 'switch <filename>'")

#print(plain_text_todo_writer({'todo': 'Second item', 'access_date': '19 Jun 2024 at 15:12', 'edited': 0, 'due': 'tomorrow'}))
#print(plain_text_todo_writer({'todo': 'Item number 3', 'access_date': '19 Jun 2024 at 15:13', 'edited': 0, 'due': 'day after tomorrow'}))
#print(plain_text_todo_parser("'Bolo bhartrihari baba ki jai' - Last edited on 'Aaj ki hi subah'"))
#print(plain_text_todo_parser("'Bolo Hanuman ji maharaj ki jai' - Last edited on 'Aaj shaam'")['todo'])