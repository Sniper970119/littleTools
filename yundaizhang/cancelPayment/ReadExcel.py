# -*- coding:utf-8 -*-

import openpyxl
from dateutil import rrule

from qichacha.FindData import FindData


class ReadExcel():
    def __init__(self):
        pass

    def read_data_excel(self, filename='file.xlsx'):
        """
        读取excel
        :param filename:
        :return:
        """
        wb = openpyxl.load_workbook(filename=filename)
        sheet1 = wb.get_sheet_by_name('Sheet2')
        col_name = sheet1['B']
        return_array = []
        for i in range(1, 188):
            name = col_name[i].value
            return_array.append(name)
        return return_array

    def read_target_excel(self, filename='result.xlsx'):
        wb = openpyxl.load_workbook(filename=filename)
        sheet1 = wb.get_sheet_by_name('Sheet1')
        serve_price = sheet1['E']
        id_sheet = sheet1['A']
        name_sheet = sheet1['B']
        begin_time = sheet1['F']
        mouth = sheet1['G']
        id = []
        price_array = []
        begin_array = []
        name_array = []
        mouth_array = []
        for i in range(1, 187):
            id.append(str(id_sheet[i].value))
            name_array.append(str(name_sheet[i].value))
            price_array.append(str(serve_price[i].value))
            begin_array.append(str(begin_time[i].value))
            mouth_array.append(str(mouth[i].value))

        return id, name_array,begin_array, price_array, mouth_array
        pass


if __name__ == '__main__':
    # ReadExcel().read_data_excel()
    ReadExcel().read_target_excel()
