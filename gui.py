##### created by boyun
##### Jul 03, 2023 13:31:31
# gui for to-do app

import functions

# using third party libraries
# find more in pypi.org
# pysimplegui

import PySimpleGUI as sg        #simplifies!

# the different instances
label = sg.Text("Type in a to-do")          #Text is the type, "" is the instance
input_box = sg.InputText(tooltip = "Enter todo", key = "todo")
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size = [45,10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

layout = [[label],
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
    event, values = window.read()
    print(1,event)
    print(2,values)
    print(3,values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = (values['todo']+"\n").capitalize()
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = (values['todo']).capitalize()

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions14.write_todos(todos)
            window['todos'].update(values=todos)        #to update in real time

        case 'todos':
            window['todo'].update(value=values['todos'][0]) #so that it shows whatever I'm selecing

        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Exit":
            break

        case sg.WIN_CLOSED:
            exit()
#use break or exit() as the last part of sg.WIN_CLOSED
# break ends the loop,

print('Bye')
window.close()