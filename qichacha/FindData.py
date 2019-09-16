# -*- coding:utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup


class FindData():
    def __init__(self):
        pass

    def find_a_data(self, name):

        # 代理服务器
        proxyHost = "http-dyn.abuyun.com"
        proxyPort = "9020"

        # 代理隧道验证信息
        proxyUser = "HF4RK2AE25YK2LXD"
        proxyPass = "2BE5A05D2A07E056"

        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }

        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }

        headers = {
            'Host': 'www.qichacha.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'QCCSESSID=16vmnadt2ti8jbto4utvq85p35; zg_did=%7B%22did%22%3A%20%2216d39386741396-0c8dd010a4d9f58-4c312373-1fa400-16d393867429f%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201568632328289%2C%22updated%22%3A%201568632375053%2C%22info%22%3A%201568623060809%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22cuid%22%3A%20%22fdddada498e13c729ce101a60af1e4a0%22%7D; UM_distinctid=16d3938677b2c3-0e98df1455889f8-4c312373-1fa400-16d3938677c55b; CNZZDATA1254842228=1399287707-1568620100-https%253A%252F%252Fsp0.baidu.com%252F%7C1568630900; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1568623061,1568627805; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1568632365; hasShow=1; _uab_collina=156862306121972474949216; acw_tc=7105b79615686230610202929ed81ce586109c76783750f21862b58907',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'

        }
        url = 'https://www.qichacha.com/search?key=' + name
        r = requests.get(url=url, headers=headers)
        url_list = re.findall('href="/(.*?).html"', r.text)
        target_url = 'https://www.qichacha.com/' + url_list[0] + '.html'
        r_target = requests.get(url=target_url, headers=headers)
        soup = BeautifulSoup(r_target.text, 'lxml')
        # 法人姓名
        bname = soup.select('.bname')
        boss_name = re.findall('>(.*?)<', str(bname))[1]
        # print("法人姓名：", boss_name)
        gen_date = ''
        social_code = ''
        people_id = ''
        regist_id = ''
        org_id = ''
        enterprise_type = ''
        industry = ''
        approve_date = ''
        log_org = ''
        region = ''
        address = ''
        # 处理其他
        for tr in soup.select('tr'):
            if '成立日期' in str(tr):
                gen_date = re.findall('"">(.*?)</td', str(tr), re.S)[1].strip().strip('\n')
                # print("成立日期：", gen_date)
            if '统一社会信用代码' in str(tr):
                social_code = re.findall('"">(.*?)</td', str(tr), re.S)[0].strip().strip('\n')
                # print("统一社会信用代码：", social_code)
            if '纳税人识别号' in str(tr):
                people_id = re.findall('"">(.*?)</td', str(tr), re.S)[1].strip().strip('\n')
                # print("纳税人识别号：", people_id)
            if '注册号' in str(tr):
                regist_id = re.findall('"">(.*?)</td', str(tr), re.S)[0].strip().strip('\n')
                # print("注册号：", regist_id)
            if '组织机构代码' in str(tr):
                org_id = re.findall('"">(.*?)</td', str(tr), re.S)[1].strip().strip('\n')
                # print("组织机构代码：", org_id)
            if '企业类型' in str(tr):
                enterprise_type = re.findall('"">(.*?)</td', str(tr), re.S)[0].strip().strip('\n')
                # print("企业类型", enterprise_type)
            if '所属行业' in str(tr):
                industry = re.findall('"">(.*?)</td', str(tr), re.S)[1].strip().strip('\n')
                # print("所属行业：", industry)
            if '核准日期' in str(tr):
                approve_date = re.findall('">(.*?)</td', str(tr), re.S)[1].strip().strip('\n')
                # print("核准日期：", approve_date)
            if '登记机关' in str(tr):
                log_org = re.findall('"">(.*?)</td', str(tr), re.S)[0].strip().strip('\n')
                # print("登记机关：", log_org)
            if '所属地区' in str(tr):
                region = re.findall('"">(.*?)</td', str(tr), re.S)[0].strip().strip('\n')
                # print("所属地区：", region)
            if '企业地址' in str(tr):
                address = re.findall('3">(.*?)<a', str(tr), re.S)[0].strip().strip('\n')
                # print("企业地址：", address)
                return_result = {
                    '公司名称': name,
                    '法定代表人': boss_name,
                    '成立日期': gen_date,
                    '统一社会信用代码': social_code,
                    '纳税人识别号': people_id,
                    '注册号': regist_id,
                    '组织机构代码': org_id,
                    '企业类型': enterprise_type,
                    '所属行业': industry,
                    '核准日期': approve_date,
                    '登记机关': log_org,
                    '所属地区': region,
                    '企业地址': address,
                }
                print(return_result, '\n')
                return return_result


if __name__ == '__main__':
    print(FindData().find_a_data('大连天地人环保科技有限公司'))
