import PySimpleGUI as sg

susunan = [
    [sg.VPush(), sg.Text("UNISKA MAB", font=("Helvetica", 24)), sg.Push()],
    [sg.VPush(), sg.Text("BANJARMASIN", font=("Courier", 18)), sg.Push()]
]

Window = sg.Window(
    title="Elemen Text",
    layout=susunan,
    size=(430, 200)
)

Window.read()

Window.close()
