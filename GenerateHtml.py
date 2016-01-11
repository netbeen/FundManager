#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def generateHtml(fundIDString, fundInfoDictList):
    templateFile = open('template.html')
    htmlContent = templateFile.read()

    htmlContent = htmlContent.replace('@fundID@',fundIDString)

    datesReplaceString = ''
    for fundInfoDict in fundInfoDictList:
        datesReplaceString += '\'' + fundInfoDict['dateString']  + '\','
    datesReplaceString = datesReplaceString[:-1]
    htmlContent = htmlContent.replace('@dates@',datesReplaceString)

    valuesReplaceString = ''
    for fundInfoDict in fundInfoDictList:
        valueString = '%.4f'%fundInfoDict['value']
        valuesReplaceString += valueString+','
    valuesReplaceString = valuesReplaceString[:-1]
    htmlContent = htmlContent.replace('@values@',valuesReplaceString)

    unitPricesReplaceString = ''
    for fundInfoDict in fundInfoDictList:
        unitPriceString = '%.4f'%fundInfoDict['unitPrice']
        unitPricesReplaceString += unitPriceString+','
    unitPricesReplaceString = unitPricesReplaceString[:-1]
    htmlContent = htmlContent.replace('@unitPrices@',unitPricesReplaceString)
   
    outputFile = open('result/'+fundIDString+'.html','w')
    outputFile.write(htmlContent)
    outputFile.close()
