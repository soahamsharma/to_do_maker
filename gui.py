from functions import get_todos, put_todos
import FreeSimpleGUI as fsg
from time import strftime

DEFAULT_FILE = 'default.txt'
extensions = ['json', 'csv', 'txt']


# Initialise the GUI components
label = fsg.Text("Enter a ToDo")
switch_file_button = fsg.Button(button_text="Change File")
todo_input_box = fsg.InputText(tooltip='ToDo goes here', key='todo')
due_input_box = fsg.InputText(tooltip='Due date goes here', key='due')
add_button = fsg.Button(button_text="Add ToDo")
edit_button = fsg.Button(button_text="Edit ToDo")
complete_button = fsg.Button(button_text="Complete ToDo")
delete_button = fsg.Button(button_text="Delete ToDo")
exit_button = fsg.Button(button_text='Exit')
window = fsg.Window('My ToDo App', layout=[[label, switch_file_button], 
                                           [todo_input_box, due_input_box, add_button], 
                                           [edit_button], 
                                           [complete_button], 
                                           [delete_button], 
                                           [exit_button]],
                    font=('Helvetica', 14))

# Program Logic
working_file = DEFAULT_FILE
counter = 0

while True:
    event, values = window.read()
    now = strftime("%d %b %Y at %H:%M")
    if event in ['Exit', fsg.WINDOW_CLOSED]:
        break
    command = event.replace(' ToDo', '') if event else ''
    match command:
        case 'Add':
            toDo = get_todos(working_file)
            toDo.append({'todo':values['todo'], 'access_date': now, 'edited': 0, 'due':values['due']})
            put_todos(toDo, working_file)

window.close()