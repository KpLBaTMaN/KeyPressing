# used to output keyboard inputs
from pynput.keyboard import Key, Controller

# used to read inputs from keyboard
import win32api
import time
from tkinter import *

# Set up
keyboard = Controller()

# Key 0,1,2,3,4,5,6,7,8,9
list_of_key_codes_buttons = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
list_of_key_codes = [0x31, 0x32, 0x33,
                     0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x30]
list_of_key_state = [False, False, False, False,
                     False, False, False, False, False, False]

toggle_on = False

master = Tk()

canvas_width = 1000
canvas_height = canvas_width/10
w = Canvas(master,
           width=canvas_width,
           height=canvas_height*1.5)
w.pack()


size_of_button = canvas_width / len(list_of_key_codes)

rectangle = []
text = []

for i in range(len(list_of_key_codes)):
    rectangle.append(w.create_rectangle(size_of_button*i, 0,
                                        (size_of_button*i)+size_of_button, size_of_button, fill='red'))

toggle_rectangle = w.create_rectangle(0, size_of_button,
                                      canvas_width, (size_of_button*1.5), fill='blue')


def task():
    for i in range(10):
        reading_input = win32api.GetKeyState(list_of_key_codes[i])
        reading_input_ctrl = win32api.GetKeyState(0x11)

        # Pressing ctrl and number
        if reading_input < 0 and reading_input_ctrl < 0:
            if(list_of_key_state[i] == True):
                list_of_key_state[i] = False
                print("Turned OFF key: " + list_of_key_codes_buttons[i])
                w.itemconfig(rectangle[i], fill='red')

            else:
                list_of_key_state[i] = True
                print("Turned ON key: " + list_of_key_codes_buttons[i])
                w.itemconfig(rectangle[i], fill='green')

    reading_input_minus = win32api.GetKeyState(0x09)
    # Pressing - key
    if reading_input_minus < 0:

        global toggle_on

        if toggle_on == True:
            toggle_on = False
            w.itemconfig(toggle_rectangle, fill='blue')
            print("Green")
            time.sleep(0.2)
        else:
            toggle_on = True
            w.itemconfig(toggle_rectangle, fill='green')
            print("Blue")
            time.sleep(0.2)

    if toggle_on == True:
        for i in range(10):
            if list_of_key_state[i] == True:
                keyboard.press(list_of_key_codes_buttons[i])
                keyboard.release(list_of_key_codes_buttons[i])
                print("Computer Press Button: " + list_of_key_codes_buttons[i])
        time.sleep(0.5)
    master.after(100, task)


master.after(100, task)
master.mainloop()


# while True:
#     # checking for inputs of the keys listed in array
#     time.sleep(1)
#     for i in range(10):
#         reading_input = win32api.GetKeyState(list_of_key_codes[i])
#         reading_input_ctrl = win32api.GetKeyState(0x11)

#         # Pressing ctrl and number
#         if reading_input < 0 and reading_input_ctrl < 0:

#             if(list_of_key_state[i] == True):
#                 list_of_key_state[i] = False
#                 print("Turned OFF key: " + list_of_key_codes_buttons[i])
#                 w.itemconfig(rectangle[i], fill='green')
#                 time.sleep(0.5)

#             else:
#                 list_of_key_state[i] = True
#                 print("Turned ON key: " + list_of_key_codes_buttons[i])
#                 w.itemconfig(rectangle[i], fill='red')
#                 time.sleep(0.5)

#     for i in range(10):
#         if list_of_key_state[i] == True:
#             keyboard.press(list_of_key_codes_buttons[i])
#             keyboard.release(list_of_key_codes_buttons[i])
#             print("Computer Press Button: " + list_of_key_codes_buttons[i])

#     print("At the end of loop")

# print("End")
