import json
import requests

# 決算スケジュールから名証ネクストなどの漏れを取得する
response = requests.get(
    "https://d1rrtoo3h22gy6.cloudfront.net/kabu-json-kessan-schedules/v1/schedules.json")

data = response.json()

# 件数チェック（1割以上減少したらエラー）
EXPECTED_MIN_COUNT = 3640  # 4044の90%
if len(data) < EXPECTED_MIN_COUNT:
    raise ValueError(f"決算データ件数が異常に少ないです。期待値: {EXPECTED_MIN_COUNT}件以上、実際: {len(data)}件")

with open("kessan.json", "w", encoding="utf-8") as json_file:
    json_file.write(json.dumps(data, ensure_ascii=False, indent=4))
