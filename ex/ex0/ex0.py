from urllib import request  # urllib.requestモジュールをインポート
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート
from urllib.error import HTTPError #エラーコード
from urllib.error import URLError
import requests, sys, csv
import pandas as pd

tables = ['albums', 'employees', 'invoices', 'playlists', 'artists', 'genres', 'media_types', 'tracks',
'customers', 'invoice_items', 'playlist_track']

header = ['id', 'name']

table = sys.argv[1]
page = sys.argv[2]
if page == str(1):
    for table_item in tables:
        if table_item == table:
            url = 'http://127.0.0.1:8080/result?name=' + table
            break
    else:
        print('tableがありません。')
else:
    for table_item in tables:
        if table_item == table:
            url = 'http://127.0.0.1:8080/result?name=' + table + '&page=' + page
            break
    else:
        print('tableがありません。')

response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")
table_ids = soup.select('.id')
datas = soup.select('.data')

table_names = soup.select('.content')

if len(table_ids) == 0:
    print('該当ページはありません。')
else:
    print('CSV出力完了しました.')    

with open('sql.csv', 'w', encoding='utf-8', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for data in datas:
        id = data.find('th', class_='id').text
        name = data.find('th', class_='content').text
        row = [id, name]
        writer.writerow(row)

df = pd.read_csv('sql.csv')
#print(df)
