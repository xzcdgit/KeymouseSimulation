import os
import time
import random
import threading
import cv2
import pyautogui

if __name__ == "__main__":
    task = threading.Thread(target=os.system, args=(r'C:\\Users\\01477483\\Desktop\\登录QQ邮箱.url',))
    task.daemon = True
    task.start()
    time.sleep(1)
    pyautogui.hotkey('alt', ' ', 'X', interval=random.random()*0.2+0.1)
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4', interval=random.random()*0.2+0.1)
    time.sleep(0.5)
