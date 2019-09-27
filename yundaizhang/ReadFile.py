# -*- coding:utf-8 -*-

import re


class ReadFile():
    def __init__(self):
        pass

    def read_file(self, file_name):
        file = open(file_name + '.data', 'r')
        input = file.readline()
        print(input)
        locations_str = re.findall('(\d{1,4}, \d{1,4})', input)
        locations_list = []
        for i in locations_str:
            locations_temp = i.split(',')
            locations_list.append((int(locations_temp[0].strip()), int(locations_temp[1].strip())))
        print(locations_list, type(locations_list))
        return locations_list
        pass


if __name__ == '__main__':
    ReadFile().read_file('hahahaha')
