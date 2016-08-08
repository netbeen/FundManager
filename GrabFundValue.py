#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request


def grabFundValue(fund_id_string, start_date_str):
    print("开始抓取基金净值，基金编号：", fund_id_string, ' 起始时间：', start_date_str)
    url_string = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=' + fund_id_string + '&page=1&per=20000'
    response = urllib.request.urlopen(url_string)
    response_string = response.read().decode('gb2312')
    tbody_index = response_string.index('<tbody>')
    tbody_end_index = response_string.index('</tbody>')
    response_string = response_string[tbody_index + 7:tbody_end_index]

    each_row_list = response_string.split('</tr><tr>')  # 使用制表分隔符切割
    each_row_list[0] = each_row_list[0][4:]
    each_row_list[-1] = each_row_list[-1][:-5]
    each_row_list.reverse()  # 逆置list，使日期递增

    fund_info_dict_list = []

    for i in range(len(each_row_list)):  # 对每一行进行拆分，提出净值和日期
        this_row = each_row_list[i]
        this_row_split_list = this_row.split('</td><td')
        this_row_split_list.pop()
        for j in range(len(this_row_split_list)):
            end_index = this_row_split_list[j].index('>')
            this_row_split_list[j] = this_row_split_list[j][end_index + 1:]
        fund_info_dict = {}
        fund_info_dict['dateString'] = this_row_split_list[0]
        fund_info_dict['value'] = float(this_row_split_list[1])
        fund_info_dict_list.append(fund_info_dict)

    start_date_index = -1
    for i in range(len(fund_info_dict_list)):
        if fund_info_dict_list[i]['dateString'] == start_date_str:
            start_date_index = i
            break

    if start_date_index == -1:
        print('错误：未找到与data文件起始日期相符的净值信息！程序即将退出!')
        exit(0)

    # print("抓取基金净值结束")
    return fund_info_dict_list[start_date_index:]
