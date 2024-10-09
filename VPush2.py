import PySimpleGUI as sg
susunan =[[sg.VPush()],
         [sg.Text("UNISKA MAB",font=("helvetica",24))],
         [sg.Text("BANJARMASIN", font=("Courier",18))],
         [sg.VPush()]]
Window =sg.Window(title="Element Text",
                   layout=susunan,
                   element_justification = "center",
                   size=(430,200))
Window.read()
Window.close()
