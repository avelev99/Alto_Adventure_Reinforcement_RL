""" Gets the key pressed by the user. """


import win32api as wpi
import win32con as wpc
import time

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
