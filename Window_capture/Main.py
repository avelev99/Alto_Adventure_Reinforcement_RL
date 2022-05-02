""" Main execution for generating screenshot data of Alto's adventure """
from Utils.Getkeys import keys
from Utils.Screencapture import WindowCapture
import cv2 as cv
import win32con as con
import numpy as np
import os
from time import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_name = "Data/screenshots.npy"
file_name2 = "Data/command_keys.npy"


def get_data():
    """Function obtained from ClarityCoders:
    https://github.com/ClarityCoders/Fall-Guys-AI/blob/master/CreateData.py"""

    if os.path.isfile(file_name):
        print("File exists, loading previous data!")
        image_data = list(np.load(file_name, allow_pickle=True))
        targets = list(np.load(file_name2, allow_pickle=True))

    else:
        print("File does not exist, starting fresh!")
        image_data = []
        targets = []

    return image_data, targets


def save_data(image_data, targets):
    """Function obtained from ClarityCoders:
    https://github.com/ClarityCoders/Fall-Guys-AI/blob/master/CreateData.py"""

    np.save(file_name, image_data)
    np.save(file_name2, targets)


def main():
    image_capture, target = get_data()
    wincap = WindowCapture("The Alto Collection")
    while True:
        print("Press 'Space' to start -- else 'q' to quit program.")
        key = keys()
        if key == 0x51:  # quit
            cv.destroyAllwindows()
            break
        if key == con.VK_SPACE:
            print("Starting Program")
            break
    loop_time = time()
    while True:
        # Get screenshot
        screenshot = wincap.get_screenshot()  # Get screenshot of window and crop
        print("FPS {}".format(1 / time() - loop_time))
        loop_time = time()
        key = keys()
        if key == 0x51:
            cv.destroyAllWindows()
            break
        if key == con.VK_SPACE:
            print("Space Bar initiated")
            image_capture.append(screenshot)
            # Get screenshot of command keys
            # We only use space bar for now
            # Once space bar goes up -> we want to record screenshot
    print("Done")
    # Save data.
    print("Finished Saving image data and target values.")


if __name__ == "__main__":
    main()
