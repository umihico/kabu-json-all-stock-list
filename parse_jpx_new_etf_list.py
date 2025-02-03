# https://www.jpx.co.jp/equities/products/etfs/issues/01.htmlをスクレイピングしてETF全銘柄コードを取得する

import requests
from lxml import html
import json

url = "https://www.jpx.co.jp/equities/products/etfs/issues/01.html"
response = requests.get(url)
tree = html.fromstring(response.content)
rows = tree.xpath("//table[@class='widetable']//tr")[1:]
# print(response.content)
print("len(rows)", len(rows))
new_stocks = []
functions = {
    "銘柄名": lambda row: row.xpath('.//td[3]')[0].text_content().split("\r\n")[1].strip().split("(注")[0],
    "コード": lambda row: row.xpath('.//td[2]')[0].text_content().strip(),
}
for (i, row) in enumerate(rows):
    new_stock = {}
    # even = i % 2 == 0
    # if not even:
    #     continue
    # next_row = rows[i + 1]
    for key, func in functions.items():
        try:
            new_stock[key] = func(row)
        except Exception as e:
            print(i, new_stock, key, e)
            raise e
    new_stocks.append(new_stock)

with open("new_etf_listings.json", "w", encoding="utf-8") as json_file:
    json_file.write(json.dumps(new_stocks, ensure_ascii=False, indent=4))
