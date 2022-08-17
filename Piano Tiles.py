import pyautogui
import time
import keyboard
import random
import win32api, win32con


print(pyautogui.position())

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(907,640)[0] == 0:
        click(907,640)
    if pyautogui.pixel(1010,640)[0] == 0:
        click(1010,640)
    if pyautogui.pixel(1093,640)[0] == 0:
        click(1093,640)
    if pyautogui.pixel(1172, 640)[0] == 0:
        click(1172, 640)
#X: 907 Y:  640
#X: 1010
#X: 1093
#X: 1172
