import datetime
import math


class ProfitRatePerYearCalculator(object):
    def __init__(self, purchase_info_dict_list):
        self.purchaseInfoDictList = purchase_info_dict_list

    def calc(self, purrent_profit_add_cost, redeem_date_string):
        last_date = datetime.datetime.strptime(redeem_date_string, '%Y-%m-%d')
        for purchaseInfoDict in self.purchaseInfoDictList:
            this_date = datetime.datetime.strptime(purchaseInfoDict['dateString'], '%Y-%m-%d')
            duration = (last_date - this_date).days
            if duration == 0:
                purchaseInfoDict['duration'] = 1
            else:
                purchaseInfoDict['duration'] = duration
        result = (self.binary_search(purrent_profit_add_cost, 0, 10) - 1) * 365
        return result

    def binary_search(self, target, low_value, high_value):
        fx = 0.0
        for purchaseInfoDict in self.purchaseInfoDictList:
            fx += purchaseInfoDict['totalPrice'] * math.pow(((low_value + high_value) / 2),
                                                            purchaseInfoDict['duration'])
        if abs(fx - target) < 0.0005:
            return (low_value + high_value) / 2
        elif (fx - target) > 0:
            return self.binary_search(target, low_value, (low_value + high_value) / 2)
        else:
            return self.binary_search(target, (low_value + high_value) / 2, high_value)
