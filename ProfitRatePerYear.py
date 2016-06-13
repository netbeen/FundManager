import datetime
import time
import math

class ProfitRatePerYearCalculator(object):
    
    def __init__(self, purchaseInfoDictList):
        print('年化利率计算器初始化：至此该基金有',len( purchaseInfoDictList ),'条购买信息')
        self.purchaseInfoDictList = purchaseInfoDictList

    def calc(self, purrentProfitAddCost, redeemDateString):
        lastDate = datetime.datetime.strptime(redeemDateString,'%Y-%m-%d')
        for purchaseInfoDict in self.purchaseInfoDictList:
           thisDate = datetime.datetime.strptime(purchaseInfoDict['dateString'],'%Y-%m-%d')
           duration = (lastDate-thisDate).days
           if duration == 0 :
               purchaseInfoDict['duration'] = 1
           else:
               purchaseInfoDict['duration'] = duration
        result =(self.binarySearch(purrentProfitAddCost,0,10)-1)*365
        return result

    def binarySearch(self, target, lowValue, highValue):
        fx = 0.0
        for purchaseInfoDict in self.purchaseInfoDictList:
            fx += purchaseInfoDict['totalPrice'] * math.pow(((lowValue+highValue) / 2) , purchaseInfoDict['duration'] )
        if abs(fx-target) < 0.0005:
            return (lowValue+highValue)/2
        elif (fx-target)>0:
            return self.binarySearch(target,lowValue,(lowValue+highValue)/2)
        else:
            return self.binarySearch(target,(lowValue+highValue)/2,highValue)
        
        
