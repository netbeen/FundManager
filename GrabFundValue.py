#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import time
import urllib.request


def grabFundValue(fundIDString, startDateStr):
    print("开始抓取基金净值，基金编号：", fundIDString, ' 起始时间：', startDateStr)
    urlString = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=' + fundIDString + '&page=1&per=20000'
    response = urllib.request.urlopen(urlString)
    responseString = response.read().decode('gb2312')
    tbodyIndex = responseString.index('<tbody>')
    tbodyEndIndex = responseString.index('</tbody>')
    responseString = responseString[tbodyIndex + 7:tbodyEndIndex]

    eachRowList = responseString.split('</tr><tr>')  # 使用制表分隔符切割
    eachRowList[0] = eachRowList[0][4:]
    eachRowList[-1] = eachRowList[-1][:-5]
    eachRowList.reverse()  # 逆置list，使日期递增

    fundInfoDictList = []

    for i in range(len(eachRowList)):  # 对每一行进行拆分，提出净值和日期
        thisRow = eachRowList[i]
        thisRowSplitList = thisRow.split('</td><td')
        thisRowSplitList.pop()
        for j in range(len(thisRowSplitList)):
            endIndex = thisRowSplitList[j].index('>')
            thisRowSplitList[j] = thisRowSplitList[j][endIndex + 1:]
        fundInfoDict = {}
        fundInfoDict['dateString'] = thisRowSplitList[0]
        fundInfoDict['value'] = float(thisRowSplitList[1])
        fundInfoDictList.append(fundInfoDict)

    startDateIndex = -1
    for i in range(len(fundInfoDictList)):
        if fundInfoDictList[i]['dateString'] == startDateStr:
            startDateIndex = i
            break

    if startDateIndex == -1:
        print('错误：未找到与data文件起始日期相符的净值信息！')

    # print("抓取基金净值结束")
    return fundInfoDictList[startDateIndex:]
