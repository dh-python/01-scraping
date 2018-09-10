#
# Pythonでスクレイピングするサンプルアプリです。
# はてなブックマークの人気一覧を取得します。
#
# 取得元：
#   http://b.hatena.ne.jp/hotentry/all
#

# 01. 必要なモジュールを読み込む.
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 02. HTMLを取得.
with urlopen("http://b.hatena.ne.jp/hotentry/all") as response:
    html = response.read().decode("utf-8")

# 03. スクレイピング（タイトルとリンクの取得）
soup = BeautifulSoup(html, "html.parser")

h3_list = soup.select(".entrylist-contents-title")
for h3 in h3_list:
    a = h3.find("a")
    title = a.string
    href = a["href"]
    print(title)
    print(href)
    print("------")