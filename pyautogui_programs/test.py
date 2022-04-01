import pyautogui

print(pyautogui.position())
# For teams leave button `Point(x=1184, y=27)`
string = "Hello guys, Aditya is wonderful person. His brother name is Aravind. This being typed by me only" \
         " Thank You!\n"
for i in range(10):
    pyautogui.click(533, 97)
    pyautogui.click(712, 567)
    pyautogui.typewrite(string)




