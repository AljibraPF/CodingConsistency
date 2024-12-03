#Drawing triangle with pyautogui

import pyautogui
import time
import math

print("Starting in 3 seconds. Move mouse to drawing area.")

time.sleep(3)

center_x, center_y = pyautogui.position()
side_length = 200
angle_step = 120
starting_angle = 90

pyautogui.mouseDown()

for i in range(3):
    next_x = center_x + side_length * math.cos(math.radians(starting_angle + i * angle_step))
    next_y = center_y - side_length * math.sin(math.radians(starting_angle + i * angle_step))

    pyautogui.moveTo(next_x, next_y)

pyautogui.mouseUp

print("Triangle done.")