##### created by boyun
##### Jul 03, 2023 13:31:31
# gui for todo app

import functions14

# using third party libraries
# find more in pypi.org
# pysimplegui

import PySimpleGUI as sg        #simplifies!

# the different instances
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo")
add_button = sg.Button('Add')

# mother instance
window = sg.Window('My Todo App',layout=[[label], [input_box, add_button]])
window.read()
window.close()