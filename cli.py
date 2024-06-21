from functions import get_todos, put_todos, pretty_print_all_todo_files, pretty_print_todos, plain_text_todo_writer
from time import strftime

DEFAULT_FILE = 'default.txt'
extensions = ['json', 'csv', 'txt']

def main():

    working_file = DEFAULT_FILE
    print("")
    pretty_print_all_todo_files(working_file, extensions)
    
    while True:
        next = input("What would you like to do? (Type 'help' to view a list of available commands.)").split()
        if next == []:
            continue
        else:
            command = next[0].lower()
        now = strftime("%d %b %Y at %H:%M")
        match command:
            case('help'):
                print("")
                print('    show - Shows all todos in the Active file')
                print('    add - Add a new todo item. Usage: "add <todo-text>". User is prompted for an optional due date')
                print('    edit - Edit an existing todo itm. Usage: "edit <todo-number> todo_text" to change todo text or "edit <todo-number> due date" to edit due date.')
                print('    delete - Delete a todo item or entire todo list. Usage: "delete <todo-number>" to delete single item or "delete all" to clear entire list')
                print('    switch - Change active file. Uses an exsiting file or creates a new one if does not exist. Usage: "switch <filepath>"  - supported file types: txt, csv')
                print('    quit - quits the program.')
                print('  Note: Todos are saved to file automatically after each operation')
                print("")
            case'show':
                toDo = get_todos(working_file)
                pretty_print_todos(toDo)      
            case 'delete':
                if len(next) != 2:
                    print('Usage: delete <to-do number | all>')
                    continue
                toDo = get_todos(working_file)
                if next[1].lower() == 'all':
                    conf = input("You sure you want to clear the entire todo-list? (yes to confirm)")
                    if conf.lower() == 'yes':
                        print('to-do list cleared')
                        toDo = []
                    else:
                        print('Deletion not confirmed')
                else:    
                    try:
                        delIndex = int(next[1])
                        delItem = toDo.pop(delIndex - 1)
                        print('Deleted', '"'+delItem['todo']+'"', 'from the to-do-list')
                    except (IndexError, ValueError) as e:
                        print(f"Please mention a valid item number to delete. There are currently {len(toDo)} items in the to-do list")
                put_todos(toDo, working_file)
            case 'add':
                toDo = get_todos(working_file)
                body_text = ' '.join(next[1:]).capitalize()
                print('Adding', '"'+body_text+'"', 'to the to-do list')
                optional_due_date = input("Provide optional due date. Press enter to save without due date. : ") 
                due = optional_due_date if optional_due_date else None
                toDo.append({'todo':body_text, 'access_date': now, 'edited': 0, 'due':due})
                put_todos(toDo, working_file)
            case 'edit':
                toDo = get_todos(working_file)
                try:
                    editIndex = int(next[1])
                    to_edit = next[2]                
                except:
                    print("Usage: 'edit <to-do number> <todo_text | due_date>'")
                    continue
                if editIndex > len(toDo):
                    print("The list has",len(toDo),"item(s).")
                else:
                    print('Current todo item:', plain_text_todo_writer(toDo[editIndex-1]))
                    if to_edit == 'todo_text':
                        new_text = input('Please enter new text: ').strip().capitalize()
                        toDo[editIndex-1]['todo'] = new_text
                        toDo[editIndex-1]['edited'] = 1
                        toDo[editIndex-1]['access_date'] = now
                        print('Edited todo item:', plain_text_todo_writer(toDo[editIndex-1]))
                    elif to_edit == 'due_date':
                        new_due = input('Please enter new due date: ').strip().capitalize()
                        toDo[editIndex-1]['due'] = new_due
                        toDo[editIndex-1]['edited'] = 1
                        toDo[editIndex-1]['access_date'] = now
                        print('Edited todo item:', plain_text_todo_writer(toDo[editIndex-1]))
                    else:
                        print("Usage: 'edit <to-do number> <todo_text | due_date>'")
                put_todos(toDo, working_file)
            case 'quit':
                print("Program Quitting.")
                break
            case 'switch':
                if len(next) != 2 or not next[1].split('.')[-1] in extensions:
                    print("Uage: 'switch <filename>'")
                    continue
                newfile = next[1]
                toDo = get_todos(newfile)
                pretty_print_todos(toDo)     
                working_file = newfile
            case _:
                print("I dunno what you said")



if __name__ == "__main__":
    main()