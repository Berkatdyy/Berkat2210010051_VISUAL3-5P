import PySimpleGUI as sg


sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")


layout = [
    [sg.Text("FTI UNISKA", font=("Helvetica", 24))],
    [sg.Text("FAKULTAS TEKNOLOGI INFORMASI", font=("Courier", 18, "bold italic underline"))]
]


Window = sg.Window(title="Profile", layout=layout, size=(430, 200), font=("Times", 18))

Window.read()

Window.close()
