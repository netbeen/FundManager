#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import time
from GrabFundValue import grabFundValue
from LoadData import loadPurchaseData
from GenerateHtml import generateHtml

if(__name__=='__main__'):
    currentDateString = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    print("当前时间：",currentDateString)

    purchaseInfoDictListDict = loadPurchaseData()

    for (key,value) in purchaseInfoDictListDict.items():
        print('开始处理',key)
        fundInfoDictList = grabFundValue(key,value[0]['dateString'])
        
        thisFundPurchaseInfoDictList = purchaseInfoDictListDict[key]
        currentCost = 0
        currentShare = 0
        nextPurchaseInfoDictIndex = 0
        for fundInfoDict in fundInfoDictList:
            if fundInfoDict['dateString'] == thisFundPurchaseInfoDictList[nextPurchaseInfoDictIndex]['dateString']:
                currentCost += thisFundPurchaseInfoDictList[nextPurchaseInfoDictIndex]['totalPrice']
                currentShare +=  thisFundPurchaseInfoDictList[nextPurchaseInfoDictIndex]['totalPrice']/fundInfoDict['value']
                nextPurchaseInfoDictIndex += 1
            fundInfoDict['unitPrice'] = currentCost / currentShare  #计算每份持仓成本

        for fundInfoDict in fundInfoDictList:
            fundInfoDict['profitRate'] = (fundInfoDict['value']-fundInfoDict['unitPrice']) / fundInfoDict['unitPrice']  #计算收益率

        #print(fundInfoDictList)
        generateHtml(key,fundInfoDictList)
