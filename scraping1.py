
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from text_ctl import insert_break_after_token

def beut122():
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
    bsObj = BeautifulSoup(html.read(), 'html.parser')
    #print(bsObj.h1)
    #print(dir(bsObj))
    #insert_break_after_token(dir(bsObj), '\'')
    for data in dir(bsObj):
        print(data)

def beut123():
    try:
        html = urlopen("http://www.pythonscraping.com/pages/page1.html")
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The sever could not be found!")
    else:
        print("It Worked!")

def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.h1
    except AttributeError as e:
        return None
    return title

def beut123_2():
    title = get_title("http://www.pythonscraping.com/pages/page1.html")
    if title == None:
        print("title could not be found")
    else:
        print(title)


if __name__ == '__main__':
    beut123_2()