# -*- coding:utf-8 -*-
import requests


class GetCustomPageList:
    def __init__(self):
        pass

    def get(self):
        """
        获取用户列表
        :return:
        """
        headers = {
            'Cookie': 'tq_source_page_url=http://www.yundaizhang.com/main.html!ctype^3D1*uid^3D17615150827*qyh^3D745163*radom^3D6.18870677716945; tracqinfo={r$"511561982168012"#ct$12#tt$0#lv$"2019-9-27^2C15^3A19^3A14"#lt$""#pu$""#cn$""#ib$0#bt$0#lb$1568714848899#ci$""#cr$""#pt$""}; 745163admin=745163admin; ASP.NET_SessionId=m2na301nmcyohhai3o4nvugc; tq_current_visit_time=1569568693917; tq_current_source_page_url=http://www.yundaizhang.com/main.html!ctype^3D1*uid^3Dadmin*qyh^3D745163*radom^3D98.60242184373476',
            'Host': 'www.yundaizhang.com',
            'Referer': 'http://www.yundaizhang.com/Manage/CRM/Custom.htm?radom=0.14521422952524787&qyh=745163',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'X-Requested-With': 'XMLHttpRequest'
        }

        data = {
            'keys': 'GetCustomPageList',
            'Wdate': '2019-09',
            'type': 'pager',
            'page': '1',
            'pageSize': '500',
            'datas': '[]',
            'CnameVal': 'k',
            'HYStatus': '1',
            'order': '2'
        }
        r = requests.post(url='http://www.yundaizhang.com/Manage/Ajax/CRMHandler.ashx', data=data, headers=headers)
        f = open('customPageData.txt', 'w+')
        f.write(r.text)
        print(r.status_code)


if __name__ == '__main__':
    GetCustomPageList().get()