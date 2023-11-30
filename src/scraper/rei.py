import httpx #libary yang digunakan untuk mengoneksikan http

from typing import Any #dari modul typing mengimport typedata Any --> semua jenis type data
from selectolax.parser import HTMLParser
from rich import print #supaya ketika print ada warnanya

class ReiSpider(object):
    def __init__(self)-> None:
        pass

    def get_product_detail(self, url: str):
        headers: dict[str, Any] = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"} #agar tidak terdeteksi sebgai bot
        response = httpx.get(url=url, headers=headers) #untuk mengambil respon dari url target

        #langkah sesudah mendapatkan data
        f = open("response_detail.html", 'w+', encoding="UTF-8") #buat ngecek file apabila terbloking
        f.write(response.text)
        f.close()

        soup: HTMLParser = HTMLParser(response.text)
        
        #data mentah
        scripts = soup.css_first("script#modelData")
        


        #scraping proses

