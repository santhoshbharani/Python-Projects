import pyautogui as spam
import time
limite=(10)
msg=("Hi")
i=0
time.sleep(10)
while i <int(limite):
     spam.typewrite(msg)
     spam.press("Enter")
i+=1
