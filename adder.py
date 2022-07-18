from distutils import extension
import glob
import os
from pathlib import Path
from time import sleep

import pyautogui as gui

path = Path(os.getcwd())

extension = glob.glob(os.getcwd()+"/*.crx")

shorts = glob.glob(str(path.parent.absolute())+"/shorts/*")
for i in range(len(shorts)):
    Command = "start "+shorts[i]+" "+extension[0]
    print(Command)
    os.system(Command)
    sleep(2)
    gui.press(['left', 'enter'])
    sleep(2)
    gui.hotkey('alt', 'd')
    gui.write("chrome-extension://eojdckfcadamkapabechhbnkleligand/index.html#/admin/dashboard")
    gui.press("enter")
    sleep(0.5)
    gui.hotkey('ctrl', 'd')
    sleep(0.5)
    os.system("taskkill /IM chrome.exe /F")