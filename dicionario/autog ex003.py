import pyautogui
from time import sleep


pyautogui.press('win')
sleep(0.5)
pyautogui.write('Paint', interval=0.5)
pyautogui.press('Enter')
sleep(0.5)

distancia = 300
pyautogui.moveTo(363, 249)
while distancia >0:
    pyautogui.drag(distancia, 0, duration=2)
    distancia -= 20
    pyautogui.drag(0, distancia, duration=2)
    pyautogui.drag(-distancia, 0, duration=2)
    distancia -= 20
    pyautogui.drag(0, -distancia, duration=2)
sleep(0.2)
