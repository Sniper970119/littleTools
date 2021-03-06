# -*- coding:utf-8 -*-

import openpyxl

from qichacha.FindData import FindData


class ReadExcel():
    def __init__(self):
        self.find_data = FindData()
        pass

    def read_excel(self, filename='file.xlsx'):
        wb = openpyxl.load_workbook(filename=filename)
        sheet1 = wb.get_sheet_by_name('Sheet2')
        col_name = sheet1['A']
        for i in range(0, len(col_name)):
            print('公司编号：', i+1)
            import time
            import random
            time.sleep(random.randint(5, 10))
            try:
                find_result = self.find_data.find_a_data(col_name[i].value)
            except:
                import logging
                logging.error(col_name[i].value)
                # print(col_name[i].value)
                continue
            # 填写法人
            temp_var = 'B' + str(i + 1)
            sheet1[temp_var] = find_result['法定代表人']
            temp_var = 'C' + str(i + 1)
            sheet1[temp_var] = find_result['登记机关']
            temp_var = 'D' + str(i + 1)
            sheet1[temp_var] = find_result['企业地址']
            temp_var = 'E' + str(i + 1)
            sheet1[temp_var] = find_result['所属行业']
            temp_var = 'F' + str(i + 1)
            sheet1[temp_var] = find_result['统一社会信用代码']
            temp_var = 'H' + str(i + 1)
            sheet1[temp_var] = find_result['成立日期']
            wb.save('result.xlsx')

            pass


if __name__ == '__main__':
    ReadExcel().read_excel()
