import pyautogui, os

print(pyautogui.size())
print(pyautogui.position())
pyautogui.moveTo(100, 300, duration=1)
pyautogui.moveRel(200, 0, duration=1)
pyautogui.moveRel(0, -100, duration=1)
# pyautogui.click(153, 745)
# pyautogui.rightClick()
pyautogui.moveTo(741, 372)
pyautogui.typewrite("# added a comment", interval=0.5)
pyautogui.hotkey("ctrl", "o")
filename = os.getcwd() + "/" + "1.jpg"
pyautogui.screenshot(filename)
pyautogui.locateCenterOnScreen(filename)
