import pyautogui
import time
from captcha import *
import os

last_sell_time = time.time()  # To keep track of when you last clicked the sell button




folder_path = "captcha"  # Replace with the path to your folder

# Let's say you have 100 pictures (or replace 100 with the number you have)
for i in range(1, 10):  # Change 101 to one more than the number of pictures you have
    file_path = os.path.join(folder_path, f"{i}.PNG")
    
    if os.path.exists(file_path):
        # Do whatever you want with the file, e.g., print its name
        captcha=solve_captcha(file_path)
        print(captcha)
    else:
        print(f"File {file_path} not found!")

print("Fishing...")
while True:
    # Click the "Fish again" button
    fish_location = pyautogui.locateCenterOnScreen('images/fish_button.png', confidence=0.9)
    if fish_location:
        pyautogui.click(fish_location)
        time.sleep(2.9)  # Wait 3.5 seconds before trying again

    # Every 300 seconds, click the "Sell" button
    current_time = time.time()
    if current_time - last_sell_time >= 300:
        sell_location = pyautogui.locateCenterOnScreen('images/sell_button.png', confidence=0.9)
        if sell_location:
            pyautogui.click(sell_location)
        last_sell_time = current_time  # Update the last sell time

    captcha_location = pyautogui.locateCenterOnScreen('images/captcha.PNG', confidence=0.95)
    if captcha_location:
        break

    time.sleep(0.1)  # General delay to prevent 100% CPU usage
