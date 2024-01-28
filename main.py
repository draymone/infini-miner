import pyautogui
import keyboard
import time

# Config fields
SLOT_X = 809
SLOT_Y = 1011
SLOT_WIDTH = 40
HOTKEYS = ["&", "é", "\"", "'", "(", "-", "è", "_", "ç", "à"]

running = True


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
    time.sleep(1.6)
    pyautogui.mouseUp()


def on_x_pressed(e):
    # Stop running the program
    global running
    running = False
    # Unsubscribe
    keyboard.unhook_all()


################
# MAIN PROGRAM #
################

# Inform the user
print("Press X to start the program")
print("Press X again to stop")

# Wait until the player starts the program
keyboard.wait("X")
time.sleep(0.1)

# Subscribe to the on x key pressed event (stops the program)
keyboard.on_press_key("X", on_x_pressed)

pickaxe_slot = 0
# Main loop
while running:
    # If there is always a pickaxe in the slot
    if pyautogui.pixel(SLOT_X + pickaxe_slot * SLOT_WIDTH, SLOT_Y) == (135, 102, 39):
        click(600, 900)
    else:
        # Else parse the other slots searching
        for i in [j for j in range(9) if j != pickaxe_slot]:
            # When a right slot is found
            if pyautogui.pixel(SLOT_X + i * SLOT_WIDTH, SLOT_Y) == (135, 102, 39):
                print(f"Switching to pickaxe {i+1}")
                # Define it as the actual slot
                pickaxe_slot = i
                keyboard.press_and_release(HOTKEYS[i])

                click(600, 900)

                break
            else:
                # Else set temporarily the slot to -1
                pickaxe_slot = -1
        # If the slot is always -1
        if pickaxe_slot == -1:
            # Stop the program
            running = False

# When the loop execution ends, shut down the program
print("Shutting down...")
print("(Press Escape to continue)")
keyboard.wait('esc')
