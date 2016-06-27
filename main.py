#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import time
from GrabFundValue import grabFundValue
from LoadData import loadPurchaseData
from GenerateHtml import generateHtml
from ProfitRatePerYear import ProfitRatePerYearCalculator

if(__name__=='__main__'):
    currentDateString = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    print("当前时间：",currentDateString)

    purchaseInfoDictListDict = loadPurchaseData()

    for (key,value) in purchaseInfoDictListDict.items():
        print('-------------------------')
        print('开始处理',key)
        fundInfoDictList = grabFundValue(key,value[0]['dateString'])
        
        thisFundPurchaseInfoDictList = purchaseInfoDictListDict[key]
        currentCost = 0
        currentShare = 0
        nextPurchaseInfoDictIndex = 0
        for fundInfoDict in fundInfoDictList:
            if nextPurchaseInfoDictIndex == len(thisFundPurchaseInfoDictList):
                pass
            elif fundInfoDict['dateString'] == thisFundPurchaseInfoDictList[nextPurchaseInfoDictIndex]['dateString']:
                currentCost += thisFundPurchaseInfoDictList[nextPurchaseInfoDictIndex]['totalPrice']
                currentShare +=  thisFundPurchaseInfoDictList[nextPurchaseInfoDictIndex]['totalPrice']/fundInfoDict['value']
                nextPurchaseInfoDictIndex += 1
            fundInfoDict['unitPrice'] = currentCost / currentShare  #计算每份持仓成本

        for fundInfoDict in fundInfoDictList:
            fundInfoDict['profitRate'] = (fundInfoDict['value']-fundInfoDict['unitPrice']) / fundInfoDict['unitPrice']  #计算收益率

        redeemFeeRate = 0.5 / 100

        nextPurchaseInfoDictIndex = 0
        currentDateString = ""
        for fundInfoDict in fundInfoDictList:
            #print(fundInfoDict['dateString'])
            currentDateString = fundInfoDict['dateString']
            untilTheDayPurchaseInfoDictList = []
            if nextPurchaseInfoDictIndex >= len(thisFundPurchaseInfoDictList):
                untilTheDayPurchaseInfoDictList = thisFundPurchaseInfoDictList
            elif fundInfoDict['dateString'] == thisFundPurchaseInfoDictList[nextPurchaseInfoDictIndex]['dateString']:
                nextPurchaseInfoDictIndex += 1
                untilTheDayPurchaseInfoDictList = thisFundPurchaseInfoDictList[0:nextPurchaseInfoDictIndex]
            else:
                untilTheDayPurchaseInfoDictList = thisFundPurchaseInfoDictList[0:nextPurchaseInfoDictIndex]
            calculator = ProfitRatePerYearCalculator(untilTheDayPurchaseInfoDictList)
            
            currentCost = 0
            for i in range(0,nextPurchaseInfoDictIndex):
                currentCost += thisFundPurchaseInfoDictList[i]['totalPrice']
            currentProfitAddCost = (fundInfoDict['profitRate'] - redeemFeeRate) * currentCost + currentCost
            fundInfoDict['profitRatePerYear'] =  calculator.calc(currentProfitAddCost,fundInfoDict['dateString'])

        print('结束时间：',currentDateString)
        print('总成本：',currentCost)
        print('利润率：',fundInfoDictList[-1]['profitRate'],'%')
        #generateHtml(key,fundInfoDictList)
        generateHtml(key,currentCost,fundInfoDictList[-1]['profitRate'],fundInfoDictList)
