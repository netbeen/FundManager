#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def loadPurchaseData():
    purchaseInfoDictListDict = {}

    if os.path.isdir('data'):
        fileList = os.listdir('data')
        print('data文件：', fileList)

        for fileName in fileList:
            purchaseInfoDictList = []
            purchaseInfoDictListDict[fileName] = purchaseInfoDictList
            fullFileName = 'data/' + fileName
            inputFile = open(fullFileName)
            line = inputFile.readline()
            while line:
                purchaseInfoDict = {}
                line = line[:-1]
                print('DEBUG:', line)
                lineSplitList = line.split('\t')
                purchaseInfoDict['dateString'] = lineSplitList[0]
                purchaseInfoDict['totalPrice'] = float(lineSplitList[1])
                purchaseInfoDictList.append(purchaseInfoDict)
                line = inputFile.readline()
            print(purchaseInfoDictListDict)
    else:
        print('错误：data文件夹不存在！程序即将退出！')
    return purchaseInfoDictListDict
