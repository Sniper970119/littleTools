import json
import time
import requests
import akshare as ak

# 512480   159792  sz000001  600150


COLUMNS = ['日期', '收盘价', '涨跌幅', '主力净流入-净额', '主力净流入-净占比', '超大单净流入-净额',
           '超大单净流入-净占比',
           '大单净流入-净额', '大单净流入-净占比', '中单净流入-净额', '中单净流入-净占比', '小单净流入-净额',
           '小单净流入-净占比']


def get_all_A_res():
    url = "https://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get"
    url = "https://push2his.eastmoney.com/api/qt/stock/kline/get"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    }
    params = {
        "klt": "101",
        "fqt": "1",
        "beg": "0",
        "secid": f"47.800000",
        "fields1": "f1,f2,f3,f4,f5,f6",
        "fields2": "f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61",
        "ut": "fa5fd1943c7b386f172d6893dbfba10b",
        "cb": "jQuery351041109404218918244_1740670627388",
        "lmt": "100000",
        "_": int(time.time() * 1000),
    }
    r = requests.get(url, params=params, headers=headers)
    r_text = r.text
    r_json = json.loads(r_text[r_text.find('(', 1) + 1:-2])
    # f51       f52     f53         f54       f55       f56      f57       f58   f59   f60    f61
    # 日期     开盘价    收盘价     最高点     最低点     成交量     成交额       振幅  涨跌幅  涨跌额  换手率
    # 2001-01-02,2002.73,2026.83,2026.96,2000.80,13252578,21944031918.00,0.00,0.00,0.00,0.02"
    # 2025-02-27,5379.69,5383.73,5392.76,5323.70,1469743882,2004242792448.00,1.28,0.06,3.19,2.08
    content_list = r_json["data"]["klines"]
    temp = content_list[-1]
    final_list = {}
    for item in content_list:
        item_list = item.split(",")
        final_list[item_list[0]] = item_list
    return final_list


all_A_res = get_all_A_res()


def get_stock_info(stock_id, market):
    stock_individual_fund_flow_df = ak.stock_individual_fund_flow(stock=stock_id, market=market)
    stock_data = stock_individual_fund_flow_df.values.tolist()
    return stock_data


sh_stock_data = get_stock_info("000001", "sh")
sz_stock_data = get_stock_info("399001", "sz")
# sh = sh_stock_data[-1]
# sz = sz_stock_data[-1]
final_stock_data = []
for i in range(len(sh_stock_data)):
    # change datetime.date to string
    sh_stock_data[i][0] = str(sh_stock_data[i][0])
    sh_stock_data[i][3] += sz_stock_data[i][3]
    sh_stock_data[i][5] += sz_stock_data[i][5]
    sh_stock_data[i][7] += sz_stock_data[i][7]
    sh_stock_data[i][9] += sz_stock_data[i][9]
    sh_stock_data[i][11] += sz_stock_data[i][11]
    final_stock_data.append(sh_stock_data[i])
    # final_stock_data[str(sh_stock_data[i][0])] = sh_stock_data[i]

final_show_list = []
for i in range(len(final_stock_data)):
    cur_stock_data = final_stock_data[i]
    cur_date = cur_stock_data[0]
    all_A_data = all_A_res[cur_date]
    chengjiaoe = float(all_A_data[6]) / 10 ** 8
    last_30_chengjiao = ''
    huanshou = float(all_A_data[-1])
    A_max = float(all_A_data[3])
    A_min = float(all_A_data[4])
    A_final = float(all_A_data[2])
    A_ratio = f'{all_A_data[-3]}%'
    boss = cur_stock_data[3] / 10 ** 8
    up_count = ''
    down_count = ''
    up_ratio = ''
    super_max_count = 1000+cur_stock_data[5] / 10 ** 8
    max_count = 1000+cur_stock_data[7] / 10 ** 8
    mid_count = 1000+cur_stock_data[9] / 10 ** 8
    small_count = 1000+cur_stock_data[11] / 10 ** 8
    cur_res = [cur_date, chengjiaoe, last_30_chengjiao, huanshou, A_max, A_min, A_final, A_ratio, boss, up_count,
               down_count, up_ratio, super_max_count, max_count, mid_count, small_count]
    final_show_list.append(cur_res)

# change final_Show_list to xlsx
import pandas as pd
#
COLUMNS = ['日期', "全A成交额", '最后30分钟成交额', '换手率', 'A最高', 'A最低', 'A收盘', '全A涨跌', '主力', "上涨",
           "下跌", '占比', '超大单成交额', '大单成交额', '中单成交额', '小单成交额']
df = pd.DataFrame(final_show_list, columns=COLUMNS)
df.to_excel("final_show_list1.xlsx", index=False)
print()
