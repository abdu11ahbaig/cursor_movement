import pyautogui
import time
import logging
from math import sin, cos, pi

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def move_in_d_shape():
    screen_width, screen_height = pyautogui.size()
    logging.info(f"Screen size detected: {screen_width}x{screen_height}")

    try:
        while True:
            start_x = screen_width // 4
            start_y = screen_height // 4
            pyautogui.moveTo(start_x, start_y, duration=0.5)
            logging.info(f"Moved to start position ({start_x}, {start_y})")

            end_y = start_y + screen_height // 2
            pyautogui.moveTo(start_x, end_y, duration=2)
            logging.info(f"Moved to vertical end position ({start_x}, {end_y})")

            radius = screen_height // 4
            center_x = start_x + radius
            center_y = start_y + radius

            for angle in range(0, 181, 5):
                x = center_x + radius * cos(angle * pi / 180)
                y = center_y + radius * sin(angle * pi / 180)
                pyautogui.moveTo(x, y, duration=0.1)

            logging.info("Completed 'D' shape movement")

            time.sleep(30)

    except KeyboardInterrupt:
        logging.info("Script terminated by user")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    logging.info("Mouse mover script started")
    move_in_d_shape()
    logging.info("Mouse mover script ended")
