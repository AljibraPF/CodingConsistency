#Pyautogui code to move the cursor in a circle

import pyautogui
import math
import time

print("Starting in 3 seconds. Move your mouse to the drawing area.")
time.sleep(3)

center_x, center_y = pyautogui.position()
radius = 100  
steps = 360  

for angle in range(steps):
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))
    
    pyautogui.moveTo(x, y, duration=0.01)
