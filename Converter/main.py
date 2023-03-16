import PySimpleGUI as sg

layout = [
    [sg.Text("Give a input and choose a measurement", key="textField"), sg.Spin(["km to miles",
                                                                                 "miles to km",
                                                                                 "kg to pound",
                                                                                 "pound to kg"], key="spin")],
    [sg.Input(key="input")],
    [sg.Button("Convert", key="convertButton"), sg.Button("Exit", key="exitButton")]
]

window = sg.Window("Converter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "convertButton":
        if values["spin"] == "km to miles":
            result = float(values["input"]) * 0.621371
            window["textField"].update(str(round(result, 2)) + " miles")

        elif values["spin"] == "miles to km":
            result = float(values["input"]) / 0.621371
            window["textField"].update(str(round(result, 2)) + " kg")

        elif values["spin"] == "kg to pounds":
            result = float(values["input"]) * 2.20462
            window["textField"].update(str(round(result, 2)) + " pounds")

        elif values["spin"] == "pounds to kg":
            result = float(values["input"]) / 2.20462
            window["textField"].update(str(round(result, 2)) + " kg")

    if event == "exitButton":
        break

window.close()
