# -*- coding:utf-8 -*-

import pynput

from pynput import mouse


def on_move(x, y):
    print('Pointer moved to {o}'.format((x, y)))


def on_click(x, y, button, pressed):
    if button == mouse.Button.right:
        print(button, type(button))
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        return False


def on_scroll(x, y, dx, dy):
    print('scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))


# while True:
import datetime

a =datetime.datetime.now()
while datetime.datetime.now() - a < datetime.timedelta(seconds=5):
    with mouse.Listener(no_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()
