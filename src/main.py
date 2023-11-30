from selectolax.parser import HTMLParser

from scraper.rei import ReiSpider #untuk memanggil scraper dari rei.py
from scraper.debug import ReiSpiderDebug

def main():
    spider: ReiSpider = ReiSpider()
    spider.get_product_detail(url = "https://www.rei.com/product/203929/la-sportiva-tarantula-climbing-shoes-mens") #memanggil fungsi get_product_detail

def debug(): #digunakan untuk menjalankan debug
    spider: ReiSpiderDebug = ReiSpiderDebug()
    with open("response_detail.html", "r", encoding="UTF-8") as html_file:
        soup = HTMLParser(html=html_file.read())
        spider.get_product_detail(soup=soup)

if __name__ == "__main__":
    debug() #didalam main.py kemudian kita menjalankan debug.py