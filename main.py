import requests as req
import sys
from bs4 import BeautifulSoup as bs

def get_imdb(query):
    page = req.get(f"https://google.com/search?q={query}")
    if page.status_code == 200:
        page = page.text
    else:
        return ('IMDb ratings not available!')
    
    s = bs(page,'html5lib')
    try:
        IMDb = s.find('div',class_="BNeawe s3v9rd AP7Wnd").get_text()
    except AttributeError:
        return None
    try:
        title = s.find('div',class_="BNeawe deIvCb AP7Wnd").get_text()
        date = s.find("span",class_="BNeawe tAd8D AP7Wnd").get_text()
        date = date.split(" ")
        date = date[2]
        print(title,end=" (")
        print(date + ")")
    except (TypeError,AttributeError):
        pass
    IMDb = IMDb.split('\n')
    IMDb[-1] = "Description: " + IMDb[-1]
    return "\n".join(IMDb)
            
def main():

    if len(sys.argv)>=3 and sys.argv[1]=="-m":
        query = "+".join(sys.argv[2].split(" "))
       # print(query)
        res = get_imdb(query)
        if res != None:
            print(res)
        else:
            print('No valid search results!')

main()
