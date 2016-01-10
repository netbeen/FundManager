#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import time
import urllib.request

def grabFundValue(fundIDString, startTimeStr):
    print("开始抓取基金净值")
    urlString = 'http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code='+fundIDString+'&page=1&per=3'
    response = urllib.request.urlopen(urlString)
    responseString = response.read().decode('gb2312')   
    tbodyIndex = responseString.index('<tbody>')
    tbodyEndIndex = responseString.index('</tbody>')
    responseString = responseString[tbodyIndex+7:tbodyEndIndex]

    eachRowList = responseString.split('</tr><tr>')     #使用制表分隔符切割
    eachRowList[0] = eachRowList[0][4:]
    eachRowList[-1] = eachRowList[-1][:-5]
    eachRowList.reverse()   #逆置list，使日期递增

    fundInfoDictList = []

    for i in range(len(eachRowList)):
        thisRow = eachRowList[i]
        thisRowSplitList = thisRow.split('</td><td')
        thisRowSplitList.pop()
        for j in range(len(thisRowSplitList)):
            endIndex = thisRowSplitList[j].index('>')
            thisRowSplitList[j] = thisRowSplitList[j][endIndex+1:]
        fundInfoDict = {}
        fundInfoDict['dateString'] = thisRowSplitList[0]
        fundInfoDict['value'] = float(thisRowSplitList[1])
        fundInfoDictList.append(fundInfoDict)
        #print(thisRowSplitList)

    print(fundInfoDictList)
    print("抓取基金净值结束")
    return

if(__name__=='__main__'):
    currentDateString = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    print("当前时间：",currentDateString)
    grabFundValue('160119',currentDateString)
