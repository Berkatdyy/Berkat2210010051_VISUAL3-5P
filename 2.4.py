import PySimpleGUI as sg

sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")

layout = [
    [sg.Text("FTI UNISKA", font=("Helvetica", 24), text_color="#FFFFFF")],
    [sg.Text("FAKULTAS TEKNOLOGI INFORMASI", font=("Courier", 18, "italic bold underline"))],
    [sg.Text("UNISKA MAB BANJARMASIN", text_color="#FFCC00")]
]

Window = sg.Window(
    title="Profile",
    layout=layout,
    size=(430, 200),
    font=("Times", 18)
)

Window.read()

Window.close()
