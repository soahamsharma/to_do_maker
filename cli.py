from functions import get_todos, put_todos, all_todo_files, pretty_print_all_todo_files, plain_text_todo_writer, pretty_print_todos
from time import strftime
import glob

default_file = 'default.txt'
extensions = ['json', 'csv', 'txt']

def main():

    working_file = default_file
    pretty_print_all_todo_files(working_file, extensions)
    
    while True:
        next = input("What would you like to do? ").split()
        if next == []:
            continue
        else:
            command = next[0].lower()
        now = strftime("%d %b %Y at %H:%M")
        match command:
            case'show':
                toDo = get_todos(working_file)
                pretty_print_todos(toDo)      
            case 'delete':
                if len(next) != 2:
                    print('Usage: delete <to-do number>')
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
                    new_text = next[2]
                    new_text = " ".join(next[2:]).title()
                except:
                    print("Usage: 'edit <to-do number> <new text>'")
                    continue
                if editIndex > len(toDo):
                    print("The list has",len(toDo),"item(s).")
                else:
                    old_item = toDo[editIndex-1]['todo']
                    print("Changed item at to-do no.", editIndex, "from", '"'+old_item+'"', 'to', '"'+new_text+'"')
                    toDo[editIndex-1]['todo'] = new_text
                    toDo[editIndex-1]['edited'] = 1
                    toDo[editIndex-1]['access_date'] = now
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