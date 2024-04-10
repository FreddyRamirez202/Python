import cv2
import numpy as np
import pyautogui
import keyboard

fps = 15.0
resolution = pyautogui.size()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter('recorded.mp4',
                      fourcc,
                      fps,
                      resolution)

while True:
    frame = np.array(pyautogui.screenshot())
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    out.write(frame)
    
    if keyboard.is_pressed('e'):
        break
    
out.release() 
cv2.destroyAllWindows()
