#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def generateHtml(fundIDString, fundInfoDictList):
    templateFile = open('template.html')
    htmlContent = templateFile.read()

    fundIDIndex = htmlContent.index('@fundID@')
    htmlContent = htmlContent[:fundIDIndex] + '\''+ fundIDString + '\'' + htmlContent[fundIDIndex+8:]

    datesIndex = htmlContent.index('@dates@')
    swapHtmlContent = htmlContent[:datesIndex]
    for fundInfoDict in fundInfoDictList:
        swapHtmlContent += '\'' + fundInfoDict['dateString']  + '\','
    swapHtmlContent = swapHtmlContent[:-1]
    swapHtmlContent += htmlContent[datesIndex+7:]
    htmlContent = swapHtmlContent

    valuesIndex = htmlContent.index('@values@')
    swapHtmlContent = htmlContent[:valuesIndex]
    for fundInfoDict in fundInfoDictList:
        valueString = '%.4f'%fundInfoDict['value']
        swapHtmlContent += valueString+','
    swapHtmlContent = swapHtmlContent[:-1]
    swapHtmlContent += htmlContent[valuesIndex+8:]
    htmlContent = swapHtmlContent


    unitPricesIndex = htmlContent.index('@unitPrices@')
    swapHtmlContent = htmlContent[:unitPricesIndex]
    for fundInfoDict in fundInfoDictList:
        unitPriceString = '%.4f'%fundInfoDict['unitPrice']
        swapHtmlContent += unitPriceString+','
    swapHtmlContent = swapHtmlContent[:-1]
    swapHtmlContent += htmlContent[unitPricesIndex+12:]
    htmlContent = swapHtmlContent
   
    
    print(htmlContent)
    
    outputFile = open('result/'+fundIDString+'.html','w')
    outputFile.write(htmlContent)
    outputFile.close()

