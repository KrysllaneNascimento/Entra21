from time import sleep
import pyautogui

a = input('Digite uma operação:')
pyautogui.press('win')
sleep(0.5)
pyautogui.write('Calculadora', interval=0.5)
pyautogui.press('Enter')
sleep(0.5)
pyautogui.write(a, interval=0.25)
pyautogui.press('Enter')