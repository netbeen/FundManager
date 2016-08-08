#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from GrabFundValue import grabFundValue
from LoadData import load_purchase_data
from GenerateHtml import generate_html
from ProfitRatePerYear import ProfitRatePerYearCalculator

if(__name__=='__main__'):
    current_date_string = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    print("当前时间：", current_date_string)

    purchase_info_dict_list_dict = load_purchase_data()

    for (key, value) in purchase_info_dict_list_dict.items():
        print('-------------------------')
        print('开始处理',key)
        fundInfoDictList = grabFundValue(key,value[0]['dateString'])
        
        thisFundPurchaseInfoDictList = purchase_info_dict_list_dict[key]
        currentCost = 0
        currentShare = 0
        nextPurchaseInfoDictIndex = 0
        for fundInfoDict in fundInfoDictList:
            if nextPurchaseInfoDictIndex == len(thisFundPurchaseInfoDictList):
                pass
            elif fundInfoDict['dateString'] == thisFundPurchaseInfoDictList[nextPurchaseInfoDictIndex]['dateString']:
                currentCost += thisFundPurchaseInfoDictList[nextPurchaseInfoDictIndex]['totalPrice']
                currentShare += thisFundPurchaseInfoDictList[nextPurchaseInfoDictIndex]['totalPrice']/fundInfoDict['value']
                nextPurchaseInfoDictIndex += 1
            fundInfoDict['unitPrice'] = currentCost / currentShare  #计算每份持仓成本

        for fundInfoDict in fundInfoDictList:
            fundInfoDict['profitRate'] = (fundInfoDict['value']-fundInfoDict['unitPrice']) / fundInfoDict['unitPrice']  #计算收益率

        redeemFeeRate = 0.5 / 100

        nextPurchaseInfoDictIndex = 0
        current_date_string = ""
        for fundInfoDict in fundInfoDictList:
            current_date_string = fundInfoDict['dateString']
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

        print('结束时间：', current_date_string)
        print('总成本：', currentCost)
        print('利润率：',round(fundInfoDictList[-1]['profitRate']*100,4),'%')
        print('年化收益率: ',round(fundInfoDictList[-1]['profitRatePerYear']*100,4),'%')
        generate_html(key, currentCost, fundInfoDictList[-1]['profitRate'], fundInfoDictList)
