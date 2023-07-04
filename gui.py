##### created by boyun
##### Jul 03, 2023 13:31:31
# gui for to-do app
# creating a standalone executable (see lecture 177 for windows and linux)
# here I wanted to use platypus
# watch lecture 177 from 10:45 when I have platypus figured out

import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):             #the txt file will be created if it doesn't exist yet
    with open("todos.txt", "w") as file
        pass

sg.theme("DarkGrey5")       #pysimplegui themes


clock = sg.Text('',key='clock')
label = sg.Text("Type in a to-do")          #Text is the type, "" is the instance
input_box = sg.InputText(tooltip = "Enter todo", key = "todo")
add_button = sg.Button(image_source="add.png", key="Add", tooltip="Add a todo")
#or, leave as 'add' and can add mouseover_colors = "color"
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size = [45,8])
edit_button = sg.Button('Edit')
complete_button = sg.Button(key='Complete', image_source="complete.png",tooltip="Complete")
exit_button = sg.Button('Exit')

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]
# doing this allows me to change layout more dynamically
# for example,
# button_labels = ['Close', 'apply']
# layout = []
# for bl in button_labels:
#    layout.append([sg.Button(bl)])

# mother instance
window = sg.Window('My Todo App',
                   layout=layout,
                   font=('Helvetica', 15))
# note that you need all the brackets
# and every instance has to be sg widget
while True:                 # keeps the window open
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = (values['todo'] + "\n").capitalize()
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = (values['todo']).capitalize()

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)        #to update in real time
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 15))

        case 'todos':
            window['todo'].update(value=values['todos'][0]) #so that it shows whatever I'm selecing

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 15))

        case "Exit":
            break

        case sg.WIN_CLOSED:
            exit()
#use break or exit() as the last part of sg.WIN_CLOSED
# break ends the loop,

print('Bye')
window.close()