# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pynput import keyboard


def press_callback(key):
    pass
    print(key)


def release_callback(key):
    pass
    # print(event.name)


l = keyboard.Listener(on_press=press_callback, on_release=pass)
l.start()
l.join()
