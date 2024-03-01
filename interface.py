import tkinter as tk
import serial

port = "COM3"

def transmit(data):
    data = str(data)
    with serial.Serial(port, 9600) as ser:
            ser.write(data.encode())

def drive():
    transmit(2)

def drive_left():
    transmit(11)

def drive_right():
    transmit(21)

def reverse():
    transmit(3)

def reverse_left():
    transmit(12)

def reverse_right():
    transmit(22)

def estop():
    transmit(1)

root = tk.Tk()

# Top row
tk.Button(root, text="DRIVE", command=drive, height=2, width=10, bg='green').grid(row=0, column=1)

# Middle row
tk.Button(root, text="DRIVE", command=drive_left, height=2, width=10, bg='green').grid(row=1, column=0)
tk.Button(root, text="DRIVE", command=drive_right, height=2, width=10, bg='green').grid(row=1, column=2)

# Bottom row
tk.Button(root, text="REVERSE", command=reverse_left, height=2, width=10, bg='#ADD8E6').grid(row=2, column=0)
tk.Button(root, text="REVERSE", command=reverse_right, height=2, width=10, bg='#ADD8E6').grid(row=2, column=2)
tk.Button(root, text="REVERSE", command=reverse, height=2, width=10, bg='#ADD8E6').grid(row=3, column=1)

# ESTOP button
tk.Button(root, text="ESTOP", command=estop, height=3, width=20, bg='#E6676B').grid(row=5, column=1)

root.title("Robot Control")
root.mainloop()