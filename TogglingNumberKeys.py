# used to output keyboard inputs
from pynput.keyboard import Key, Controller

# used to read inputs from keyboard
import win32api
import time

# Set up
keyboard = Controller()

# Key 0,1,2,3,4,5,6,7,8,9
list_of_key_codes_buttons = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_of_key_codes = [0x30, 0x31, 0x32, 0x33,
                     0x34, 0x35, 0x36, 0x37, 0x38, 0x39]
list_of_key_state = [False, False, False, False,
                     False, False, False, False, False, False]


while True:
    # checking for inputs of the keys listed in array
    time.sleep(1)
    for i in range(10):
        reading_input = win32api.GetKeyState(list_of_key_codes[i])
        reading_input_ctrl = win32api.GetKeyState(0x11)

        # Pressing ctrl and number
        if reading_input < 0 and reading_input_ctrl < 0:

            if(list_of_key_state[i] == True):
                list_of_key_state[i] = False
                print("Turned OFF key: " + list_of_key_codes_buttons[i])
                time.sleep(0.5)

            else:
                list_of_key_state[i] = True
                print("Turned ON key: " + list_of_key_codes_buttons[i])
                time.sleep(0.5)

    for i in range(10):
        if list_of_key_state[i] == True:
            keyboard.press(list_of_key_codes_buttons[i])
            keyboard.release(list_of_key_codes_buttons[i])
            print("Computer Press Button: " + list_of_key_codes_buttons[i])


for i in listOfNumbers:
    keyboard.press(i)
    keyboard.press(i)
