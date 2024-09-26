import PySimpleGUI as sg

sg.theme('Dark Brown')

keyboardImage = sg.Image('new-keyboard-layout-smallest.png')

layout = [[keyboardImage]]

window = sg.Window('Keyboard Layout Helper', layout, location=(1100, 600),
                   no_titlebar=True,  auto_size_buttons=False,
                   keep_on_top=False, grab_anywhere=True,
                   alpha_channel=0.5, use_default_focus=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
