# -*- coding:utf-8 -*-
from yundaizhang.cancelPayment.HandleDelete import HandleDelete
from yundaizhang.cancelPayment.ReadExcel import ReadExcel
from yundaizhang.cancelPayment.ReadJson import ReadJson

if __name__ == '__main__':
    """
    中央处理器x
    """
    json_name, json_ID = ReadJson().read()
    excel_data = ReadExcel().read_data_excel()
    id, name_array, begin_array, price_array, mouth_array = ReadExcel().read_target_excel()
    # 数据检查
    # for i in range(len(excel_data)):
    #     if excel_data[i] not in json_name:
    #         print(excel_data[i])
    #         print()

    # 删除数据
    import time

    # for i in range(1,len(excel_data)):
    #     name_index = json_name.index(excel_data[i])
    #     print('公司名：', excel_data[i], '列表索引：', name_index)
    #     current_ID = json_ID[name_index]
    #     paymentID, total = HandleDelete().find_paymentID(current_ID)
    #     while paymentID is not None:
    #         HandleDelete().delete_payment(paymentID, total)
    #         paymentID, total = HandleDelete().find_paymentID(current_ID)
    #     id = HandleDelete().find_bargain(current_ID)
    #     HandleDelete().delete_bargain(id)
    #     time.sleep(1)

    # 添加数据
    for i in range(1, 180):
        name_index = json_name.index(name_array[i])
        print('第', i, '个：公司名：', name_array[i], '列表索引：', name_index)
        current_ID = json_ID[name_index]
        HandleDelete().add_bargain(cid=current_ID, code=id[i], serve_price=price_array[i],
                                   date=begin_array[i], account_price='200', mouth=mouth_array[i])

        bargain_id = HandleDelete().find_bargain(current_ID)
        if mouth_array[i] == '1':
            money_count = 12 * int(price_array[i])
        elif mouth_array[i] == '2':
            money_count = 24 * int(price_array[i])
        else:
            money_count = int(mouth_array[i]) * int(price_array[i])
        HandleDelete().get_money(money_count, current_ID, 0, bargain_id)
        HandleDelete().get_money('200', current_ID, 1, bargain_id)
        # time.sleep(600)
    pass
