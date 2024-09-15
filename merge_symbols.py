# open generated monthly.json new_listings.json then merge them into one file

# monthly =     [{
#         "日付": 20240830,
#         "コード": 9997,
#         "銘柄名": "ベルーナ",
#         "市場・商品区分": "プライム（内国株式）",
#         "33業種コード": 6100,
#         "33業種区分": "小売業",
#         "17業種コード": 14,
#         "17業種区分": "小売",
#         "規模コード": 6,
#         "規模区分": "TOPIX Small 1"
#     }
# ]%
# new_listings =     [{
#     {
#         "上場日": "2024/02/07",
#         "上場承認日": "2023/12/25",
#         "会社名": "SOLIZE（株）",
#         "コード": "5871",
#         "市場区分": "スタンダード",
#         "会社概要": "https://www.jpx.co.jp/listing/stocks/new/bkk2ed0000004wbs-att/02SOLIZE-Outline.pdf",
#         "確認書": "https://www.jpx.co.jp/listing/stocks/new/bkk2ed0000004wbs-att/02SOLIZE-k.pdf",
#         "仮条件": "1,380～1,470",
#         "公募": "995.2",
#         "売買単位": "100",
#         "Iの部": "https://www.jpx.co.jp/listing/stocks/new/bkk2ed0000004wbs-att/02SOLIZE-1s.pdf",
#         "CG報告書": "https://www.jpx.co.jp/listing/stocks/new/bkk2ed0000004wbs-att/02SOLIZE-cg.pdf",
#         "公募・売出価格": "1,470",
#         "売出": "(OA149.2)",
#         "決算短信": "https://www.jpx.co.jp/listing/stocks/new/bkk2ed0000004wbs-att/02SOLIZE.pdf"
#     }
# ]

import json

with open("monthly.json", "r", encoding="utf-8") as json_file:
    monthly = json.load(json_file)

with open("new_listings.json", "r", encoding="utf-8") as json_file:
    new_listings = json.load(json_file)

merged_all_stocks = {}

for stock in monthly:
    merged_all_stocks[str(stock["コード"])] = {
        "コード": str(stock["コード"]),
        "銘柄名": stock["銘柄名"],
    }

for stock in new_listings:
    merged_all_stocks[str(stock["コード"])] = {
        "コード": str(stock["コード"]),
        "銘柄名": stock["会社名"],
    }

print(f"銘柄数: {len(merged_all_stocks)}")

with open("all_stocks.json", "w", encoding="utf-8") as json_file:
    json_file.write(json.dumps(list(merged_all_stocks.values()),
                    ensure_ascii=False, indent=4))
