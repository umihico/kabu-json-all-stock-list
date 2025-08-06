# https://www.sse.or.jp/listing/listをスクレイピングして札幌証券取引所の上場銘柄一覧を取得する

import requests
from lxml import html
import json

url = "https://www.sse.or.jp/listing/list"
response = requests.get(url)
tree = html.fromstring(response.content)

# 各銘柄のdt要素を取得（dtタグ内のaタグを取得）
stock_items = tree.xpath("//dt/a")
sse_stocks = []

for link in stock_items:
    # リンクテキストから証券コードと会社名を取得
    link_text = link.text_content().strip()
    # spanタグ内のコードを取得
    code = link.xpath(".//span/text()")
    if code:
        code = code[0].strip()
        # 会社名は全体のテキストからコードを除いた部分
        name = link_text.replace(code, '').strip()
        
        # 株式会社を除去したバージョンも保持（他のパーサーと一貫性を保つため）
        clean_name = name.replace('株式会社', '').replace('（株）', '')
        
        sse_stocks.append({
            "証券コード": code,
            "会社名": name,
            "会社名（簡略）": clean_name,
            "市場": "札証"
        })

# 件数チェック（1割以上減少したらエラー）
# 札証の上場企業数は約60社前後
EXPECTED_MIN_COUNT = 54  # 60の90%
if len(sse_stocks) < EXPECTED_MIN_COUNT:
    raise ValueError(f"札証上場データ件数が異常に少ないです。期待値: {EXPECTED_MIN_COUNT}件以上、実際: {len(sse_stocks)}件")

print(f"札証上場銘柄数: {len(sse_stocks)}")

with open("sse_listings.json", "w", encoding="utf-8") as json_file:
    json_file.write(json.dumps(sse_stocks, ensure_ascii=False, indent=4))