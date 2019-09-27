# -*- coding:utf-8 -*-
import json


class ReadJson:
    def __init__(self):
        pass

    def read(self):
        """
        读取json
        :return:
        """
        return_name_array = []
        return_ID_array = []
        f = open('customPageData.json', 'r', encoding='utf-8')
        data = f.read()
        # print(data)
        data_in_json = json.loads(data)
        # print(data_in_json['data'][1]['CustomerName'])
        for i in range(len(data_in_json['data'])):
            return_name_array.append(data_in_json['data'][i]['CustomerName'])
            return_ID_array.append(data_in_json['data'][i]['ID'])
        return return_name_array, return_ID_array


if __name__ == '__main__':
    ReadJson().read()
