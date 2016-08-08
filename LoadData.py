#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def load_purchase_data():
    purchase_info_dict_list_dict = {}

    if os.path.isdir('data'):
        file_list = os.listdir('data')
        print('data文件：', file_list)

        for fileName in file_list:
            purchase_info_dict_list = []
            purchase_info_dict_list_dict[fileName] = purchase_info_dict_list
            full_file_name = 'data/' + fileName
            input_file = open(full_file_name)
            line = input_file.readline()
            while line:
                purchase_info_dict = {}
                line = line[:-1]
                print('DEBUG:', line)
                line_split_list = line.split('\t')
                purchase_info_dict['dateString'] = line_split_list[0]
                purchase_info_dict['totalPrice'] = float(line_split_list[1])
                purchase_info_dict_list.append(purchase_info_dict)
                line = input_file.readline()
            print(purchase_info_dict_list_dict)
    else:
        print('错误：data文件夹不存在！程序即将退出！')
    return purchase_info_dict_list_dict
