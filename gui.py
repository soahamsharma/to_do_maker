import functions
import PySimpleGUI as sg

label = sg.Text("Label for window")
input_box = sg.InputText(tooltip="Enter Something here")
first_button = sg.Button("Pehla")
second_button = sg.Button("Doosra")

window = sg.Window("Random Window", layout=[[label],[input_box],[first_button, second_button]])
window.read()
window.close()