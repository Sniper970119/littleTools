# -*- coding:utf-8 -*-

import openpyxl
from dateutil import rrule

from qichacha.FindData import FindData


class ReadExcel():
    def __init__(self):
        self.find_data = FindData()
        pass

    def read_excel(self, filename='file.xlsx'):
        wb = openpyxl.load_workbook(filename=filename)
        sheet1 = wb.get_sheet_by_name('Sheet1')
        col_name = sheet1['A']
        end_time = sheet1['F']
        begin_time = sheet1['K']
        for i in range(2, len(col_name)):
            name = col_name[i].value
            if name is None:
                break
            sub_begin_time = str(begin_time[i].value)
            sub_end_time = str(end_time[i].value)
            print(name, sub_begin_time, sub_end_time)

            if sub_begin_time =='None' or sub_end_time is '':
                continue
            print(name, sub_begin_time, sub_end_time)
            print()
            begin = datetime.datetime.strptime(sub_begin_time, '%Y.%m')
            end = datetime.datetime.strptime(sub_end_time, '%Y%m')
            month = rrule.rrule(rrule.MONTHLY, dtstart=begin, until=end).count()
            temp_var = 'L' + str(i + 1)
            sheet1[temp_var] = month
        wb.save('result.xlsx')


if __name__ == '__main__':
    import datetime

    # sub_begin_time = '2019.7'
    # d1 = datetime.datetime.strptime(sub_begin_time, '%Y.%m')
    # print(d1)
    # sub_begin_time = '202006'
    # d = datetime.datetime.strptime(sub_begin_time, '%Y%m')
    # print(d)
    # print(rrule.rrule(rrule.MONTHLY, dtstart=d1, until=d).count())
    ReadExcel().read_excel()
