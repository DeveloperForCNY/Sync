import time

import pyautogui
import pywinauto
import ctypes
import win32com.client
import win32con

import win32gui
from pywinauto import mouse

WindowTitle = "Lunar Client (1.8.9-a8b13ac/master)"
Handle = None
Pos = None
def getWindow():
    global Handle
    try:
        window = win32gui.FindWindow(None,WindowTitle)
        Handle=window
        pos = win32gui.GetWindowRect(window)
        print("找到游戏窗口" + str(pos))
        return (pos[0], pos[1])
    except Exception as e:
        print(e)
def Start():
    global Pos
    getWindow()
    win32gui.BringWindowToTop(Handle)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(Handle)
    win32gui.ShowWindow(Handle, win32con.SW_MAXIMIZE)
    Pos = pyautogui.position()
def Mining():
    global Pos
    pyautogui.press('Esc')
    pyautogui.moveTo(Pos)
    i = 0
    left = 0
    while True:
        if left == 0:
            time.sleep(0.9)
            for x in range(1, 4):
                pyautogui.moveRel(-90, 0)
                pyautogui.mouseDown(button="left")
                time.sleep(0.9)
                if x == 4 or x == 2:
                    pyautogui.moveRel(-100, 0)
                    pyautogui.mouseDown(button="left")
                    time.sleep(0.9)
            left = 1
        if left == 1:
            pyautogui.moveRel(0, 100)
            time.sleep(0.9)
            for x in range(1,4):
                pyautogui.moveRel(90, 0)
                pyautogui.mouseDown(button="left")
                time.sleep(0.9)
                if x == 4 or x == 2:
                    pyautogui.moveRel(100, 0)
                    pyautogui.mouseDown(button="left")
                    time.sleep(0.9)
            left = 2
        if left == 2:
            pyautogui.moveRel(0, 100)
            time.sleep(0.9)
            for x in range(1,4):
                pyautogui.moveRel(-90, 0)
                pyautogui.mouseDown(button="left")
                time.sleep(0.9)
                print(90)
                if(x == 4 or x == 2):
                    pyautogui.moveRel(-100, 0)
                    pyautogui.mouseDown(button="left")
                    time.sleep(0.9)
                    print(100)
            pyautogui.moveRel(0,-200)
            pyautogui.moveRel(370,0)
            left = 0



#Start()
time.sleep(5)
Mining()
print(Handle)

