import PySimpleGUI as sg


susunan = [
    [sg.Push(), sg.Text("UNISKA MAB", font=("Helvetica", 24)), sg.Push()],
    [sg.Push(), sg.Text("BANJARMASIN", font=("Courier", 18)), sg.Push()]
]


Window = sg.Window(
    title="Elemen Text",
    layout=susunan,
    size=(430, 200)
)

Window()

Window.close()
