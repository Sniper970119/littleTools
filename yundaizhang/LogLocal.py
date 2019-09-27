# -*- coding:utf-8 -*-
from pynput import mouse


class LogLocal():
    def __init__(self):
        pass

    def log_local(self, count, name):
        def on_click(x, y, button, pressed):
            if button == mouse.Button.right and pressed:
                if len(locations) < count:
                    print(len(locations))
                    locations.append((x, y))
                else:
                    print(locations)
                    self.save_location(locations, name)
                    return locations
            if not pressed:
                return False

        locations = []
        import datetime
        a = datetime.datetime.now()
        while datetime.datetime.now() - a < datetime.timedelta(seconds=10):
            with mouse.Listener(on_click=on_click) as listener:
                listener.join()
        pass

    def save_location(self, locations, name):
        print('save data')
        files = open(name + '.data', 'w')
        files.writelines(str(locations))


if __name__ == '__main__':
    # LogLocal().save_location([(1, 2), (2, 3), (3, 4)], 'hahaha')
    LogLocal().log_local(5,'hahahaha')
    pass
