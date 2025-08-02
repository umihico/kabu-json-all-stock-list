# https://www.jpx.co.jp/listing/stocks/new/index.htmlをスクレイピングして新規上場銘柄を取得する

# <thead>

#                       <tr>
#                         <th rowspan="2" class="">上場日<br>（上場承認日）</th>
#                         <th rowspan="2">会社名<sup>（注3）</sup></th>
#                         <th>コード</th>
#                         <th>会社概要<br><sup>（注4）</sup></th>
#                         <th>確認書<br><sup>（注6）</sup></th>
#                         <th class="">仮条件（円）</th>
#                         <th>公募（千株）</th>
#                         <th>売買<br>単位</th>
#                       </tr>
#                       <tr>
#                         <th>市場区分</th>
#                         <th class="">Iの部<br><sup>（注5）</sup></th>
#                         <th class="">CG<br>報告書</th>
#                         <th>公募・売出価格<br>（円）</th>
#                         <th>売出（千株）<br><sup>（注7）</sup></th>
#                         <th>決算<br>短信<br><sup>（注8）</sup></th>
#                       </tr>

#                   </thead>
# <tbody>
#                     <tr class="bg-even">

#                               <td class="a-center tb-color001 w-space" rowspan="2">2024/10/11<br>
#                             （2024/09/05）
#                           </td>

#                       <td class="a-left tb-color001 issuename-word-break" rowspan="2">
#                       <a href="https://alt.ai/" rel="external" gid="新規上場会社情報(https://alt.ai/)" class="" target="_blank">（株）オルツ</a>
#                       </td>
#                       <td class="a-center tb-color001 xh-highlight">
#                         <span id="260A"></span>
#                         260A
#                       </td>
#                       <td class="a-center tb-color001">
#         <a href="/listing/stocks/new/mklp77000000g9zy-att/10alt-Outline.pdf" rel="external" gid="新規上場会社情報(/listing/stocks/new/mklp77000000g9zy-att/10alt-Outline.pdf)" class=""><img src="/common/images/icon/tvdivq000000019l-img/icon-pdf.png" alt="PDF" title="PDF" width="16" height="16"></a>
#       </td>
#                       <td class="a-center tb-color001">
#         <a href="/listing/stocks/new/mklp77000000g9zy-att/10alt-k.pdf" rel="external" gid="新規上場会社情報(/listing/stocks/new/mklp77000000g9zy-att/10alt-k.pdf)"><img src="/common/images/icon/tvdivq000000019l-img/icon-pdf.png" alt="PDF" title="PDF" width="16" height="16"></a>
#       </td>
#                       <td class="a-center tb-color001">-</td>
#                       <td class="a-right w-space tb-color001">7,500</td>
#                       <td class="a-right w-space tb-color001">100</td>
#                     </tr>
#                     <tr>
#                       <td class="a-center tb-color001">グロース</td>
#                       <td class="a-center tb-color001">
#         <a href="/listing/stocks/new/mklp77000000g9zy-att/10alt-1s.pdf" rel="external" gid="新規上場会社情報(/listing/stocks/new/mklp77000000g9zy-att/10alt-1s.pdf)"><img src="/common/images/icon/tvdivq000000019l-img/icon-pdf.png" alt="PDF" title="PDF" width="16" height="16"></a>
#       </td>
#                       <td class="a-center tb-color001">
#         <a href="/listing/stocks/new/mklp77000000g9zy-att/10alt-cg.pdf" rel="external" gid="新規上場会社情報(/listing/stocks/new/mklp77000000g9zy-att/10alt-cg.pdf)"><img src="/common/images/icon/tvdivq000000019l-img/icon-pdf.png" alt="PDF" title="PDF" width="16" height="16"></a>
#       </td>
#                       <td class="a-center tb-color001">-</td>
#                       <td class="a-right w-space tb-color001">1,500(OA1,350)</td>
#                       <td class="a-center tb-color001">-</td>
#                     </tr>

import requests
from lxml import html
import json

url = "https://www.jpx.co.jp/listing/stocks/new/index.html"
response = requests.get(url)
tree = html.fromstring(response.content)
rows = tree.xpath("//table[contains(@class, 'widetable')]//tbody/tr")
new_stocks = []
functions = {
    "上場日": lambda row, next_row: row.xpath('.//td[1]/text()')[0].strip(),
    "上場承認日": lambda row, next_row: row.xpath('.//td[1]/text()')[1].strip().replace("（", "").replace("）", ""),
    "会社名": lambda row, next_row: row.xpath('.//td[2]')[0].text_content().split("\r\n")[1].strip(),
    "コード": lambda row, next_row: row.xpath('.//td[3]')[0].text_content().strip(),
    "市場区分": lambda row, next_row: next_row.xpath('.//td[1]/text()')[0].strip(),
    "会社概要": lambda row, next_row: "https://www.jpx.co.jp" + row.xpath('.//td[4]/a/@href')[0].strip(),
    "確認書": lambda row, next_row: "https://www.jpx.co.jp" + row.xpath('.//td[5]/a/@href')[0].strip(),
    "仮条件": lambda row, next_row: row.xpath('.//td[6]/text()')[0].strip(),
    "公募": lambda row, next_row: row.xpath('.//td[7]/text()')[0].strip(),
    "売買単位": lambda row, next_row: row.xpath('.//td[8]/text()')[0].strip(),
    "Iの部": lambda row, next_row: "https://www.jpx.co.jp" + next_row.xpath('.//td[2]/a/@href')[0].strip(),
    "CG報告書": lambda row, next_row: str("https://www.jpx.co.jp" + next_row.xpath('.//td[3]/a/@href')[0]) if next_row.xpath('.//td[3]/text()')[0].strip() != "-" else next_row.xpath('.//td[3]/text()')[0].strip(),
    "公募・売出価格": lambda row, next_row: next_row.xpath('.//td[4]/text()')[0].strip(),
    "売出": lambda row, next_row: next_row.xpath('.//td[5]/text()')[0].strip(),
    "決算短信": lambda row, next_row: str("https://www.jpx.co.jp" + next_row.xpath('.//td[6]/a/@href')[0]) if next_row.xpath('.//td[6]/text()')[0].strip() != "-" else next_row.xpath('.//td[6]/text()')[0].strip()
}
for (i, row) in enumerate(rows):
    new_stock = {}
    even = i % 2 == 0
    if not even:
        continue
    next_row = rows[i + 1]
    for key, func in functions.items():
        try:
            new_stock[key] = func(row, next_row)
        except Exception as e:
            print(i, new_stock, key, e)
            raise e
    new_stocks.append(new_stock)

with open("new_listings.json", "w", encoding="utf-8") as json_file:
    json_file.write(json.dumps(new_stocks, ensure_ascii=False, indent=4))
