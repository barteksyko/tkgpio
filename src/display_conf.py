from tkgpio import TkCircuit

configuration = {
    "width": 925,
    "height": 600,
    "toggles": [
        {
            "x": 100,
            "y": 40,
            "name": " TO1 Start/Stop",
            "pin": 15,
        },
        {
            "x": 410,
            "y": 40,
            "name": " TO2 Start/Stop",
            "pin": 13,
        },
        {
            "x": 720,
            "y": 40,
            "name": " ODZ Start/Stop",
            "pin": 11,
        },
    ],
    "leds": [
        {"x": 140, "y": 100, "name": "TO1", "pin": 16},
        {"x": 450, "y": 100, "name": "TO2", "pin": 19},
        {"x": 760, "y": 100, "name": "ODZ", "pin": 21},
    ],
    "adc": {
        "mcp_chip": 3008,
        "potenciometers": [
            {"x": 80, "y": 170, "name": "Speed Potentiometer TO1", "channel": 0},
            {"x": 385, "y": 170, "name": "Speed Potentiometer TO2", "channel": 2},
            {"x": 695, "y": 170, "name": "Speed Potentiometer ODZ", "channel": 6},
        ],
    },
    "motors": [
        {
            "x": 120,
            "y": 230,
            "name": "Motor TO1",
            "forward_pin": 22,
            "backward_pin": 23,
        },
        {
            "x": 430,
            "y": 230,
            "name": "Motor TO2",
            "forward_pin": 26,
            "backward_pin": 23,
        },
        {
            "x": 740,
            "y": 230,
            "name": "Motor ODZ",
            "forward_pin": 20,
            "backward_pin": 23,
        },
    ],
    "lcds": [
        {
            "x": 180,
            "y": 420,
            "name": "LCD",
            "pins": [2, 3, 4, 5, 6, 7],
            "columns": 16,
            "lines": 2,
        },
        {
            "x": 500,
            "y": 420,
            "name": "LCD",
            "pins": [8, 25, 18, 14, 17, 27],
            "columns": 16,
            "lines": 2,
        },
    ],
    "labels": [
        {
            "x": 15,
            "y": 35,
            "width": 35,
            "height": 22,
            "borderwidth": 2,
            "relief": "solid",
        },
        {
            "x": 320,
            "y": 35,
            "width": 35,
            "height": 22,
            "borderwidth": 2,
            "relief": "solid",
        },
        {
            "x": 625,
            "y": 35,
            "width": 35,
            "height": 22,
            "borderwidth": 2,
            "relief": "solid",
        },
    ],
}


def run(main_function):
    circuit = TkCircuit(configuration)
    circuit.run(main_function)
