# -*- coding:"utf-8 -*-
import requests
import re


class HandleDelete:
    def __init__(self):
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'tq_source_page_url=http://www.yundaizhang.com/main.html!ctype^3D1*uid^3D17615150827*qyh^3D745163*radom^3D6.18870677716945; tracqinfo={r$"511561982168012"#ct$13#tt$0#lv$"2019-9-27^2C15^3A29^3A10"#lt$""#pu$""#cn$""#ib$0#bt$0#lb$1568714848899#ci$""#cr$""#pt$""}; 745163admin=745163admin; ASP.NET_SessionId=m2na301nmcyohhai3o4nvugc; tq_current_visit_time=1569568693917; tq_current_source_page_url=http://www.yundaizhang.com/main.html!ctype^3D1*uid^3Dadmin*qyh^3D745163*radom^3D98.60242184373476',
            'Host': 'www.yundaizhang.com',
            'Referer': 'http://www.yundaizhang.com/Manage/CRM/PaymentList.htm?_=1569574432517',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'X-Requested-With': 'XMLHttpRequest'
        }
        pass

    def find_paymentID(self, cid):
        data = {
            'action': 'getpaymentlist',
            'cid': cid,
        }
        r = requests.post(url='http://www.yundaizhang.com/Manage/Ajax/PaymentHandler.ashx', data=data,
                          headers=self.headers)
        paymentID = re.findall('"paymentID":(\d+)', r.text)[0]
        total = int(re.findall('"total":(\d+)', r.text)[0])
        if total == 0:
            return None, None

        print('收款编号:', paymentID, total)
        return paymentID, total

    def delete_payment(self, paymentID, total):

        data = {
            'action': 'cancel',
            'paymentID': paymentID,
        }
        # for i in range(total):
        r = requests.post(url='http://www.yundaizhang.com/Manage/Ajax/PaymentHandler.ashx', data=data,
                          headers=self.headers)
        msg = re.findall('"msg":"(.*?)"', r.text)[0]
        print(msg)
        if total == 1:
            return False
        return True
        pass

    def find_bargain(self, cid):
        data = {
            'action': 'getcontractlist',
            'cid': cid,
        }
        r = requests.post(url='http://www.yundaizhang.com/Manage/Ajax/ContractHandler.ashx', data=data,
                          headers=self.headers)
        _id = re.findall('"_id":(\d+),', r.text)[0]
        print('合同编号:', _id)
        return _id

    def delete_bargain(self, ids):
        data = {
            'action': 'delete',
            'ids': ids,
        }
        r = requests.post(url='http://www.yundaizhang.com/Manage/Ajax/ContractHandler.ashx', data=data,
                          headers=self.headers)
        msg = re.findall('"msg":"(.*?)"', r.text)[0]
        print(msg)

    def add_bargain(self, cid, code, serve_price, date, account_price, mouth):
        data = {"action": "add",
                "jsonData": "{'CustomerID':'" + cid + "','Code':'" + code + "','MonthPrice':'" + serve_price + "','StartDate':'" + date + "','Operator':'admin-admin','OperatorID':'1801','Remark':'','PayWayID':5,'Limit':'" + mouth + "','IsAuto':false,'IsPreway':true,'HT_Code':'','IsSign':false,'AccountBookPrice':'" + account_price + "'}",
                "code": code, "htcode": "", "fujians": "", "remark": "", "czr": "admin-admin", "qtkey": "",
                "qtvalue": "", "xq": "0"}
        da1 = {"action": "add",
               "jsonData": "{'CustomerID':'61e0348e-9d6f-49a1-a9fa-c2564b94c11b','Code':'123213','MonthPrice':'21312','StartDate':'2019-08-01','Operator':'admin-admin','OperatorID':'1801','Remark':'','PayWayID':4,'Limit':70,'IsAuto':false,'IsPreway':true,'HT_Code':'','IsSign':false,'AccountBookPrice':'20000'}",
               "code": "123213", "htcode": "", "fujians": "", "remark": "", "czr": "admin-admin", "qtkey": "",
               "qtvalue": "", "xq": "0"}
        r = requests.post(url='http://www.yundaizhang.com/Manage/Ajax/ContractHandler.ashx', data=data,
                          headers=self.headers)
        print(r.text)
        msg = re.findall('"msg":"(.*?)"', r.text)[0]
        print(msg)
        pass

    def get_money(self, count, cid, type, htid):
        assert (type in [0, 1]), 'type error'
        if type == 0:
            type_name = '%u8BB0%u8D26%u670D%u52A1%u8D39'
        else:
            type_name = '%u8D26%u672C%u8D39'
        # %u8D26%u672C%u8D39
        # %u8BB0%u8D26%u670D%u52A1%u8D39
        data = {"action": "add", "_operator": "admin-admin", "_amount": count, "_yhamount": "0",
                "_operatorid": "1801", "_customerID": cid,
                "operareDate": "2019-9-27", "costtype": type_name, "htid": htid,
                "ishtsk": "1", "isdjsk": "0", "planidarr": "", "amountarr": "", "yharr": "", "jsr": "",
                "jsrid": "", "sksj": "2019-9-27", "ht_zhid": "1130", "dj_zhid": "", "remark": "",
                "remark2": ""}
        r = requests.post(url='http://www.yundaizhang.com/Manage/Ajax/PaymentHandler.ashx', data=data,
                          headers=self.headers)
        msg = re.findall('"msg":"(.*?)"', r.text)[0]
        print(msg)


if __name__ == '__main__':
    # paymentID, total = HandleDelete().find_paymentID('61e0348e-9d6f-49a1-a9fa-c2564b94c11b')
    # while paymentID is not None:
    #     HandleDelete().delete_payment(paymentID, total)
    #     paymentID, total = HandleDelete().find_paymentID('61e0348e-9d6f-49a1-a9fa-c2564b94c11b')
    # id = HandleDelete().find_bargain('61e0348e-9d6f-49a1-a9fa-c2564b94c11b')
    # HandleDelete().delete_bargain(id)

    # 45df1343-7a28-4926-b3c5-003b517637b4

    # HandleDelete().add_bargain(cid='45df1343-7a28-4926-b3c5-003b517637b4', code='k-0001', serve_price='200',
    #                            date='2019-08-08', account_price='200', mouth='13')

    # # def get_money(self, count, cid, type):
    # HandleDelete().get_money('2600', '61e0348e-9d6f-49a1-a9fa-c2564b94c11b', 0,id)
    # HandleDelete().get_money('200', '61e0348e-9d6f-49a1-a9fa-c2564b94c11b', 1,id)
    pass
