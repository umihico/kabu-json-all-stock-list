# https://www.jpx.co.jp/markets/statistics-equities/misc/01.htmlに公開されている
# https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xlsをダウンロードして、パーズして、jsonにして出力する

import requests
import pandas as pd
import os
import json

# Define the URL to download the Excel file
url = "https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls"

# Download the file
response = requests.get(url)
filename = "data_j.xls"

# Save the file locally
with open(filename, 'wb') as file:
    file.write(response.content)

# Read the Excel file using pandas
df = pd.read_excel(filename)

# Convert the DataFrame to a JSON object
data_json = df.to_json(orient="records", force_ascii=False)

# Output the JSON to a file
with open("monthly.json", "w", encoding="utf-8") as json_file:
    json_file.write(json.dumps(json.loads(data_json),
                    ensure_ascii=False, indent=4))

# Optionally remove the downloaded Excel file to clean up
if os.path.exists(filename):
    os.remove(filename)
