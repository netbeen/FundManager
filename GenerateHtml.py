#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def generate_html(fund_id_string, total_cost, profit_rate, fund_info_dict_list):
    template_file = open('template.html')
    html_content = template_file.read()

    html_content = html_content.replace('${fundID}', fund_id_string)

    html_content = html_content.replace('${totalCost}', '%.2f' % total_cost)

    html_content = html_content.replace('${currentProfitRate}', '%.2f' % (profit_rate * 100))

    html_content = html_content.replace('${totalValue}', '%.2f' % (total_cost * (profit_rate + 1)))

    dates_replace_string = ''
    for fundInfoDict in fund_info_dict_list:
        dates_replace_string += '\'' + fundInfoDict['dateString'] + '\','
    dates_replace_string = dates_replace_string[:-1]
    html_content = html_content.replace('${dates}', dates_replace_string)

    values_replace_string = ''
    for fundInfoDict in fund_info_dict_list:
        value_string = '%.4f' % fundInfoDict['value']
        values_replace_string += value_string + ','
    values_replace_string = values_replace_string[:-1]
    html_content = html_content.replace('${values}', values_replace_string)

    unit_prices_replace_string = ''
    for fundInfoDict in fund_info_dict_list:
        unit_price_string = '%.4f' % fundInfoDict['unitPrice']
        unit_prices_replace_string += unit_price_string + ','
    unit_prices_replace_string = unit_prices_replace_string[:-1]
    html_content = html_content.replace('${unitPrices}', unit_prices_replace_string)

    profit_rate_replace_string = ''
    for fundInfoDict in fund_info_dict_list:
        profit_rate_string = '%.2f' % (fundInfoDict['profitRate'] * 100)
        profit_rate_replace_string += profit_rate_string + ','
    profit_rate_replace_string = profit_rate_replace_string[:-1]
    html_content = html_content.replace('${profitRate}', profit_rate_replace_string)

    profit_rate_per_year_replace_string = ''
    for fundInfoDict in fund_info_dict_list:
        profit_rate_per_year_string = '%.2f' % (fundInfoDict['profitRatePerYear'] * 100)
        profit_rate_per_year_replace_string += profit_rate_per_year_string + ','
    profit_rate_per_year_replace_string = profit_rate_per_year_replace_string[:-1]
    html_content = html_content.replace('${profitRatePerYear}', profit_rate_per_year_replace_string)

    output_file = open('result/' + fund_id_string + '.html', 'w')
    output_file.write(html_content)
    output_file.close()
