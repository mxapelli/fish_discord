import pyautogui
import time

last_sell_time = time.time()  # To keep track of when you last clicked the sell button

while True:
    # Click the "Fish again" button
    fish_location = pyautogui.locateCenterOnScreen('fish_button.png', confidence=0.8)
    if fish_location:
        pyautogui.click(fish_location)
        time.sleep(2.5)  # Wait 3.5 seconds before trying again

    # Every 300 seconds, click the "Sell" button
    current_time = time.time()
    if current_time - last_sell_time >= 300:
        sell_location = pyautogui.locateCenterOnScreen('sell_button.png', confidence=0.8)
        if sell_location:
            pyautogui.click(sell_location)
        last_sell_time = current_time  # Update the last sell time

    time.sleep(1)  # General delay to prevent 100% CPU usage
