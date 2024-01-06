import pyautogui
import time
from pynput import keyboard
from my_mistakes import Y_or_X


stop_autoclicker = False

def on_key_release(key):
    global stop_autoclicker
    if key == keyboard.Key.cmd:
        stop_autoclicker = True

listener = keyboard.Listener(on_release=on_key_release)
listener.start()

def auto_clicker(interval, clicks, sleepy=3):
    try:
        for i in range(1, sleepy + 1):
            print(f"Начало автокликера через {sleepy + 1 - i}")
            time.sleep(1)  # Пауза для того, чтобы вы успели переключиться на нужное окно
            if stop_autoclicker:
                raise KeyboardInterrupt
        if ansver:
            while True:
                pyautogui.click()
                time.sleep(interval)
                if stop_autoclicker:
                    raise KeyboardInterrupt
        else:
            for _ in range(clicks):
                pyautogui.click()
                time.sleep(interval)
                if stop_autoclicker:
                    raise KeyboardInterrupt
    except KeyboardInterrupt:
        print()
        print('Автокликер завершен досрочно.')
    else:
        print("Автокликер завершен нормально.")
        

if __name__ == '__main__':
    print('Нужен бесконечный кликер?')

    while True:
        try:
            ansver = input('y/n: ')
            intervals = float(input('Введите интерал: '))
            if ansver not in ['y', 'n', 'Y', 'N']:
                raise Y_or_X
            else:
                break

        except ValueError:
            print('Введите корректные данные')

        except Y_or_X:
            print('Введите y or n')
            
    if ansver == 'y':
        ansver = True
        num = 0

    else:
        ansver = False
        num = int(input('Введите кол-во кликов: '))

    auto_clicker(interval=intervals, clicks=num, sleepy=3)
