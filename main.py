import time
import pyautogui as pg
from directKeys import click_l, click_r, queryMousePosition, moveMouseTo
import keyboard
from ctypes import Structure, c_long

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def auto_clicker_l(mouse_pos, clicks):
    global is_running
    for i in range(clicks):
        if keyboard.is_pressed('q'):  # Press 'q' to stop the autoclick
            is_running = False
            return
        click_l(mouse_pos.x, mouse_pos.y) # left
        time.sleep(0.02)

def auto_clicker_r(mouse_pos, clicks):
    global is_running
    for i in range(clicks):
        if keyboard.is_pressed('q'):  # Press 'q' to stop the autoclick
            is_running = False
            return
        click_r(mouse_pos.x, mouse_pos.y) # right
        time.sleep(0.02)

def create_coords(x, y):
    pos = POINT()
    pos.x = x
    pos.y = y
    return pos

def def_coords():
    global ass_slap, ingame_clicker, hearts, cat, exp, upgrade, coin, hand, gauntlet, feet, shoes
    ass_slap = create_coords(995, 500)
    ingame_clicker = create_coords(1868, 166)
    hearts = create_coords(809, 946)
    cat = create_coords(1217, 818)
    exp = create_coords(959, 942)
    upgrade = create_coords(952, 413)
    coin = create_coords(1108, 940)
    hand = create_coords(1401, 334)
    gauntlet = create_coords(830, 598)
    feet = create_coords(1220, 781)
    shoes = create_coords(450, 597)

# Start the auto clicker by pressing 's' and stop by pressing 'q'
if __name__ == "__main__":
    is_running = False
    index = 0
    def_coords()
    
    while True:
        if keyboard.is_pressed('s') and not is_running:  # Press 's' to start the autoclick
            is_running = True
            
            while is_running:
                """ mousepos = queryMousePosition()
                auto_clicker_l(mousepos, 600) """
                """ auto_clicker_l(ingame_clicker, 3)
                time.sleep(0.3) """

                auto_clicker_l(ass_slap, 900) # clicks for ass slapping
                time.sleep(0.2)

                """ auto_clicker_l(ingame_clicker, 3)
                time.sleep(0.3) """

                pg.click(hearts.x, hearts.y) # open hearts shop
                time.sleep(0.2)
                auto_clicker_l(cat, 10) # auto click the cat 
                time.sleep(0.4)

                pg.click(coin.x, coin.y) # open equipment shop
                time.sleep(0.5)
                index += 1
                index %= 3
                auto_clicker_l(hand if index == 0 else feet, 3) # open hands shop
                time.sleep(0.5)
                auto_clicker_r(gauntlet if index == 0 else shoes, 10) # auto click the gauntlet
                time.sleep(0.4)

                pg.click(exp.x, exp.y) # open exp shop
                time.sleep(0.2)
                auto_clicker_l(upgrade, 32) # auto click the upgrade
                time.sleep(0.4)

                keyboard.press_and_release("escape") # exit shop
                time.sleep(0.2)
        
        if keyboard.is_pressed('q'):  # Press 'q' to exit the program
            is_running = False
            break
