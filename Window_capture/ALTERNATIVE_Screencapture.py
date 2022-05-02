""" This program captures screenshot and the key pressed by the user at the time of the screenshot."""


import win32api as wpi
import win32con as wpc
import time
import cv2
import numpy as np


keyList = [wpc.VK_SPACE, 0x51]


def keys():
    """Retrieves the associated key with snapshot."""
    keys_array = []
    for key in keyList:
        if isinstance(key, int):
            if wpi.GetAsynckeyState(key):
                keys_array.append(key)
    if wpc.VK_SPACE in keys_array:
        return wpc.VK_SPACE
    elif 0x51 in keys_array:  # 'Q' for quit.
        return 0x51


def screen_capture(x1, y1, x2, y2):
    """Captures screenshot."""
    hwin = wpi.GetDesktopWindow()
    width = wpi.GetSystemMetrics(wpc.SM_CXVIRTUALSCREEN)
    height = wpi.GetSystemMetrics(wpc.SM_CYVIRTUALSCREEN)
    left = wpi.GetSystemMetrics(wpc.SM_XVIRTUALSCREEN)
    top = wpi.GetSystemMetrics(wpc.SM_YVIRTUALSCREEN)

    hwindc = wpi.GetWindowDC(hwin)
    srcdc = wpi.CreateCompatibleDC(hwindc)
    memdc = wpi.CreateCompatibleDC(hwindc)

    bmp = wpi.CreateCompatibleBitmap(hwindc, width, height)
    wpi.SelectObject(memdc, bmp)
    wpi.BitBlt(memdc, 0, 0, width, height, srcdc, left, top, wpc.SRCCOPY)

    signedIntsArray = wpi.GetBitmapBits(bmp, height * width * 4)
    img = np.frombuffer(signedIntsArray, dtype='uint8')
    img.shape = (height, width, 4)

    wpi.DeleteObject(bmp)
    wpi.DeleteDC(srcdc)
    wpi.DeleteDC(memdc)
    wpi.ReleaseDC(hwin, hwindc)

    return img


def main():
    """Main function."""
    print("Press 'Q' to quit.")
    while True:
        if keys() == 0x51:  # 'Q' for quit.
            break
        else:
            img = screen_capture(640, 360, 1280, 720)
            cv2.imshow('Screen', img)
            cv2.waitKey(1)


if __name__ == '__main__':
    main()