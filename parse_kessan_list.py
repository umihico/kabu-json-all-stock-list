import json
import requests

# 決算スケジュールから名証ネクストなどの漏れを取得する
response = requests.get(
    "https://d1rrtoo3h22gy6.cloudfront.net/kabu-json-kessan-schedules/v1/schedules.json")

data = response.json()

with open("kessan.json", "w", encoding="utf-8") as json_file:
    json_file.write(json.dumps(data, ensure_ascii=False, indent=4))
