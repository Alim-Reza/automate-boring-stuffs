import pyautogui
import time
import random

# print(pyautogui.position())
# print(pyautogui.size())


def click(x_co_ordinates, y_co_ordinates, sleep_time):
    time.sleep(sleep_time)
    pyautogui.click(x=x_co_ordinates, y=y_co_ordinates, clicks=1, interval=0, button='left') 

def write(text, sleep_time):
    time.sleep(sleep_time)
    pyautogui.typewrite(text)

def click_chrome():
    click(1335, 387, 2)

def wishy_wish(bandar_name, message):
    click(1218, 286, 2)  # search bar icon
    write(bandar_name, 2) 
    click(998, 437, 5) # click on the name
    write(message, 2)
    time.sleep(2)
    pyautogui.press('enter')
    click(1180, 334, 2) # close the chatbar

def main_process(list_of_colleague, message):
    random_sleep_time = random.randint(0, 3) 
    for i in list_of_colleague:
        wishy_wish(i, message)
        time.sleep(random_sleep_time)
        
list_of_colleague = []

def initiating_the_process(message):
    pyautogui.press('win')
    write('chrome', 1)
    pyautogui.press('enter')
    write('facebook.com', 1)
    pyautogui.press('enter')
    time.sleep(5)
    main_process(list_of_colleague, message)

initiating_the_process('happy new year')