import pyautogui    # pip install pyautogui
import keyboard     # pip install keyboard
import pytesseract  # pip install pytesseract
from PIL import Image, ImageGrab 
import tkinter as tk

from pynput import mouse # pip install pynput
from PIL import ImageGrab

import easyocr # pip install easyocr
from translate import Translator # pip install translate


# Создаем обработчик события нажатия кнопки мыши
def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        print('HelloWorld - проверка работы задержки')

    if not pressed:
        # Если кнопка мыши отпущена, останавливаем обработчик
        return False
    

def capture_screen():
    # Запоминаем координаты мыши
    x1, y1 = pyautogui.position()
    print(x1,y1)

    # Ждем, пока не будет нажата левая кнопка мыши
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    # Запоминаем координаты мыши после нажатия левой кнопки
    x2, y2 = pyautogui.position()
    print(x2,y2)

    #screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))


    # Захватываем область экрана между двумя координатами и извлекаем текст
    try:
        
        screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
        screenshot.save("E:\Python\Projects\Tests\ScreenTranslator\screenshot.png")
        print('Слева на право',x1, y1, x2, y2)
        print(screenshot)
    
    except Exception as e:
        print(e)
        
        # Меняем координаты что бы всегда были точки отсчета меньшие (тоесть просто строим рамку с "зеркальных углов")
        print('Справа на лево',x1, y1, x2, y2)
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
      
        screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
        screenshot.save("E:\Python\Projects\Tests\ScreenTranslator\screenshot.png")
        

    path = 'E:\Python\Projects\Tests\ScreenTranslator\screenshot.png'
    reader = easyocr.Reader(['en','ru'])   # Объект с распознаванием -  Языки которые будет искать на скрине (['ru','ch_sim','en']) 
    result = reader.readtext(path, detail=0, paragraph=True)    # Если нет detail=0 то Выводит координаты текста, сам текст , точность распознавания

    result_string = ''.join(result)
    print("\nРезультат: ",result_string)


    translator = Translator(to_lang="ru")
    translation = translator.translate(result_string)

    print('Перевод: ',translation)


    
if __name__ == "__main__":
    keyboard.add_hotkey("9", capture_screen)
    # Ожидание нажатия клавиши "9"
    keyboard.wait()


'''
    Hello world.

    This is testing screen capture translator.

    Whish me good luck!

    Долбаные коммиты!!!!

'''

