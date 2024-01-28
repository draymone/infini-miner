import pyautogui
import time
import keyboard

while not keyboard.is_pressed('q'):
    time.sleep(1)


def click(x, y):
    """
    Hold the click for 3 seconds on the point at coordinates x, y
    :param x: x coordinate for clicked point
    :param y: y coordinate for clicked point
    :return:
    """
    # Move the mouse at the right coordinates
    pyautogui.moveTo(x, y)
    # Hold the click for 3 seconds
    pyautogui.mouseDown()
    time.sleep(3)
    pyautogui.mouseUp()


# Main loop
while not keyboard.is_pressed('.'):

    if pyautogui.pixel(799, 1062)[0] == 135:
        while pyautogui.pixel(799, 1062)[0] == 135:
            keyboard.press_and_release('1')
            click(900, 600)

    if pyautogui.pixel(838, 1062)[0] == 135:
        while pyautogui.pixel(838, 1062)[0] == 135:
            keyboard.press_and_release('2')
            click(900, 600)

    if pyautogui.pixel(879, 1062)[0] == 135:
        while pyautogui.pixel(879, 1062)[0] == 135:
            keyboard.press_and_release('3')
            click(900, 600)

    if pyautogui.pixel(919, 1062)[0] == 135:
        while pyautogui.pixel(919, 1062)[0] == 135:
            keyboard.press_and_release('4')
            click(900, 600)

    if pyautogui.pixel(959, 1062)[0] == 135:
        while pyautogui.pixel(959, 1062)[0] == 135:
            keyboard.press_and_release('5')
            click(900, 600)

    if pyautogui.pixel(999, 1062)[0] == 135:
        while pyautogui.pixel(999, 1062)[0] == 135:
            keyboard.press_and_release('6')
            click(900, 600)

    if pyautogui.pixel(1039, 1062)[0] == 135:
        while pyautogui.pixel(1039, 1062)[0] == 135:
            keyboard.press_and_release('7')
            click(900, 600)

    if pyautogui.pixel(1079, 1062)[0] == 135:
        while pyautogui.pixel(1079, 1062)[0] == 135:
            keyboard.press_and_release('8')
            click(900, 600)

    if pyautogui.pixel(1119, 1062)[0] == 135:
        while pyautogui.pixel(11192, 1062)[0] == 135:
            keyboard.press_and_release('9')
            click(900, 600)