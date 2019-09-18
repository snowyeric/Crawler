# 下載GOOGLE動圖

# [MAC] SSL Cerificate FAIL
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import os

# 把我要引用的檔案名稱打在尾巴
from urllib.request import urlopen, urlretrieve
import json

#指定下載年份
years = ["2018", "2019"]

for y in years:
    # 每個月份的檔案我都要
    for m in range(1,13):
        # 把18.19年各月份的照片
        url = "https://www.google.com/doodles/json/"+str(y)+"/"+str(m)+"?hl=zh_TW"
        # 發現url是一個list
        print(url)
        # 把抓下來的URL轉換成python讀得懂的編碼
        resoponse = urlopen(url)
        # doodles經過存取後，我發現它是一個dict
        doodles = json.load(resoponse)
        print("doodles={}".format(doodles))
        print("----------------------------------------")
        # 處理dict裡面的資料
        for d in doodles:
            print(d)
            print("------------------------------------------")
            url = "https:" + d["url"]
            print(d["title"], url)
            #[-1]代表，我要把網頁透過"/"切開後，下載最後一個圖片檔，不指定檔名是因為圖檔的形式很多，非單一形式
            url.split("/")[-1]
        #為每個不同的年分(月份)創資料夾
            dirname = "doodles/" + str(y) + "/" + str(m) + "/"
            path = dirname + url.split("/")[-1]
            # 因為我懶，所以如果資料夾不存在，我就請作業系統幫我創一個新的
            if not os.path.exists(dirname):
                os.makedirs(dirname)
        #下載檔案
        urlretrieve(url, path)