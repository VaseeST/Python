import PySimpleGUI as sg


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font="Calibri 14", button_element_size=(6, 3))
    button_size = (6, 3)
    layout = [
        # Output field
        [sg.Text(
            "0",
            font="Calibri 50",
            justification="right",
            expand_x=True,
            pad=(10, 20),
            right_click_menu=theme_menu,
            key="textField")
         ],
        # First line
        [sg.Button("Enter", expand_x=True),
         sg.Button("Clear", expand_x=True)
         ],
        # Second line
        [sg.Button("7", size=button_size, expand_x=True),
         sg.Button("8", size=button_size, expand_x=True),
         sg.Button("9", size=button_size, expand_x=True),
         sg.Button("*", size=button_size, expand_x=True)
         ],
        # Third line
        [sg.Button("4", expand_x=True),
         sg.Button("5", expand_x=True),
         sg.Button("6", expand_x=True),
         sg.Button("/", expand_x=True)
         ],
        # Fourth line
        [sg.Button("1", expand_x=True),
         sg.Button("2", expand_x=True),
         sg.Button("3", expand_x=True),
         sg.Button("+", expand_x=True)
         ],
        # Fifth line
        [sg.Button("0", expand_x=True),
         sg.Button(".", size=button_size),
         sg.Button("-", size=button_size)
         ],
    ]

    return sg.Window("Calculator", layout)


theme_menu = ["Menu", ["Black", "LightGrey1", "BluePurple", "random"]]
window = create_window("Black")

current_num = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        current_num.append(event)
        num_string = "".join(current_num)
        window["textField"].update(num_string)

    if event in ["+", "-", "*", "/"]:
        full_operation.append("".join(current_num))
        current_num = []
        full_operation.append(event)
        window["textField"].update("")

    if event == "Enter":
        full_operation.append("".join(current_num))
        result = eval(" ".join(full_operation))
        window["textField"].update(result)
        full_operation = []
        current_num = [str(result)]

    if event == "Clear":
        current_num = []
        full_operation = []
        window["textField"].update("0")

window.close()
