# -*- encoding:utf-8 -*-
import pymongo

from_client_ip = input("原始服务器ip:")
to_client_ip = input("目的服务器ip:")
from_client = pymongo.MongoClient('mongodb://' + from_client_ip + ':27017/')
to_client = pymongo.MongoClient('mongodb://' + to_client_ip + ':27017/')
print('原始服务器数据库结构：')
print(from_client.list_database_names())
for from_database_name in from_client.list_database_names():
    # 控制台输出判断
    need_handle = input("是否需要处理数据库" + from_database_name + "(y/n)：")
    if need_handle is 'n':
        print("放弃该数据库")
        continue
    # 将获取到的就服务器数据库名转化为数据库对象
    from_database = from_client[from_database_name]
    # 新服务器创建数据库
    print("新建数据库" + from_database_name)
    to_client_database = to_client[from_database_name]
    for from_collection_name in from_database.collection_names():
        # 将获取到的就服务器集合名转化为集合对象
        from_collection = from_database[from_collection_name]
        # 新服务器创建集合
        print("\t|-->新建集合" + from_collection_name+ '\t(' + str(from_collection.count())+')')
        to_client_collection = to_client_database[from_collection_name]
        # 数据复制
        try:
            to_client_collection.insert(from_collection.find())
        except:
            # 如果没有数据，添加测试数据，防止集合不创建
            temp_comment = {'xx': '11'}
            to_client_collection.insert_one(temp_comment)
