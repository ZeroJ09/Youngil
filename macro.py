import pyautogui
import keyboard
import time

catch = True

print("심심해서 만든 매크로, 사용시 관련된 문제는 책임지지 않음\n-------------------------------------\nMade by ZeroJ\n-------------------------------------")
print("원하는 강좌에 마우스 올리고 a누르기\n중간종료는 ctrl+alt+del")

while True:
    if keyboard.read_key() == "a":
        Want = pyautogui.position()
        break

while catch:
    try:
        pyautogui.moveTo("cancel.png")
        catch = False
    except:
        pyautogui.moveTo(Want)
        pyautogui.click(Want)
        time.sleep(0.5)
        pyautogui.click(1063,160)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'r')
