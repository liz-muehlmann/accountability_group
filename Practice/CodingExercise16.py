# building a GUI

import PySimpleGUI as sg

label1 = sg.Text("Enter feet: ")
inputBox1 = sg.InputText(key="feet")
label2 = sg.Text("Enter inches: ")
inputBox2 = sg.InputText(key="inches")
convert_button = sg.Button('Convert')
output_label = sg.Text(key="output")

window = sg.Window('Convertor',
                   layout=[[label1,inputBox1],
                           [label2,inputBox2],
                           [convert_button,output_label]])

while True:
    event, values = window.read()
    print(1,event)
    print(2,values)
    match event:
        case "Convert":
            meters = 0.3 * int(values["feet"]) + 0.025 * int(values["inches"])
            window["output"].update(value=f"{meters}m")


window.read()
window.close()