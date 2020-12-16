from features.steps.brower_setting import Browser
import json
from features.steps.parse_methods import collect_date_filter, company_price, \
    percent_increase, company_list, company_dividends


class Dict(Browser):

    def parse_dict_to_json(self):
        try:
            with open("report.json", "w", encoding="utf-8") as file:
                json.dump(collect_date_filter, file, indent=4, ensure_ascii=False, separators=(',', ': '))
        except IOError as e:
            print(e)
            assert False

    # def write_to_json2(self):

    # for i in range(len(company_price)):
    # for company_list, dividends in dict_dividends.items():
    # collect_date_filter.update({
    # company_list:
    # {
    # 'price': company_price[i],
    # 'percent': percent_increase[i],
    # 'dividends': dividends
    # }
    # })
    # print(collect_date_filter)
    # return collect_date_filter

    def write_to_json1(self):

        for i in range(len(company_price)):
            print(collect_date_filter)
            collect_date_filter.update({
                company_list[i]:
                    {
                        'price': company_price[i],
                        'percent': percent_increase[i],
                        'dividends': company_dividends[i]
                    }
            })
        print(collect_date_filter)
        return collect_date_filter
