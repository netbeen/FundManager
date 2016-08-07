#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def generateHtml(fundIDString, totalCost, profitRate, fundInfoDictList):
    templateFile = open('template.html')
    htmlContent = templateFile.read()

    htmlContent = htmlContent.replace('${fundID}',fundIDString)

    htmlContent = htmlContent.replace('${totalCost}','%.2f'%totalCost)

    htmlContent = htmlContent.replace('${currentProfitRate}','%.2f'%(profitRate*100))

    htmlContent = htmlContent.replace('${totalValue}','%.2f'%(totalCost*(profitRate+1)))

    datesReplaceString = ''
    for fundInfoDict in fundInfoDictList:
        datesReplaceString += '\'' + fundInfoDict['dateString']  + '\','
    datesReplaceString = datesReplaceString[:-1]
    htmlContent = htmlContent.replace('${dates}',datesReplaceString)

    valuesReplaceString = ''
    for fundInfoDict in fundInfoDictList:
        valueString = '%.4f'%fundInfoDict['value']
        valuesReplaceString += valueString+','
    valuesReplaceString = valuesReplaceString[:-1]
    htmlContent = htmlContent.replace('${values}',valuesReplaceString)

    unitPricesReplaceString = ''
    for fundInfoDict in fundInfoDictList:
        unitPriceString = '%.4f'%fundInfoDict['unitPrice']
        unitPricesReplaceString += unitPriceString+','
    unitPricesReplaceString = unitPricesReplaceString[:-1]
    htmlContent = htmlContent.replace('${unitPrices}',unitPricesReplaceString)

    profitRateReplaceString = ''
    for fundInfoDict in fundInfoDictList:
        profitRateString = '%.2f'%(fundInfoDict['profitRate']*100)
        profitRateReplaceString += profitRateString+','
    profitRateReplaceString = profitRateReplaceString[:-1]
    htmlContent = htmlContent.replace('${profitRate}',profitRateReplaceString)
    
    profitRatePerYearReplaceString = ''
    for fundInfoDict in fundInfoDictList:
        profitRatePerYearString = '%.2f'%(fundInfoDict['profitRatePerYear']*100)
        profitRatePerYearReplaceString += profitRatePerYearString+','
    profitRatePerYearReplaceString = profitRatePerYearReplaceString[:-1]
    htmlContent = htmlContent.replace('${profitRatePerYear}',profitRatePerYearReplaceString)
    
    outputFile = open('result/'+fundIDString+'.html','w')
    outputFile.write(htmlContent)
    outputFile.close()
