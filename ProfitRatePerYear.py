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
           #print('天数差距: ',lastDate.strftime('%Y-%m-%d'),' - ',thisDate.strftime('%Y-%m-%d'),(lastDate - thisDate).days)
           duration = (lastDate-thisDate).days
           if duration == 0 :
               purchaseInfoDict['duration'] = 1
           else:
               purchaseInfoDict['duration'] = duration
        print(self.purchaseInfoDictList)
        result =(self.binarySearch(purrentProfitAddCost,0,100)-1)*365
        print(result)
        print('---------------')
        return result

    def binarySearch(self, target, lowValue, highValue):
        fx = 0.0
        for purchaseInfoDict in self.purchaseInfoDictList:
            #print(purchaseInfoDict['duration'])
            #print('x^t',math.pow((lowValue+highValue)/2,purchaseInfoDict['duration']))
            fx += purchaseInfoDict['totalPrice'] * math.pow(((lowValue+highValue) / 2) , purchaseInfoDict['duration'] )
        #print(target,' ' ,fx,' ', lowValue,' ', highValue)
        if abs(fx-target) < 0.0005:
            #print('error: ',fx-target,' err abs:',abs(fx-target))
            return (lowValue+highValue)/2
        elif (fx-target)>0:
            return self.binarySearch(target,lowValue,(lowValue+highValue)/2)
        else:
            return self.binarySearch(target,(lowValue+highValue)/2,highValue)
        
        
