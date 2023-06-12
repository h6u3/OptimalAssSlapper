import time
import pyautogui
from directKeys import click, queryMousePosition
import keyboard

def auto_clicker():
    is_running = False
    while True:
        if keyboard.is_pressed('s') and not is_running:  # Press 's' to start the autoclick
            is_running = True
            #keyboard.press('F6')
            while is_running:
                if keyboard.is_pressed('q'):  # Press 'q' to stop the autoclick
                    is_running = False
                    #keyboard.press('F6')
                    break
                mouse_pos = queryMousePosition()
                click(mouse_pos.x, mouse_pos.y)
                time.sleep(0.001)
        elif keyboard.is_pressed('q'):  # Press 'q' to exit the program
            break

# Start the auto clicker by pressing 's' and stop by pressing 'q'
if __name__ == "__main__":
    auto_clicker()
