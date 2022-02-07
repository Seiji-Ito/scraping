from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
from text_ctl import write_dirdata_to_textfile

def youtube_scrape():
    # urlopen
    try:
        html = urlopen("https://www.youtube.com/watch?v=gmvLh7c3PpM")
    except HTTPError as e:
        print(e)

    # html parse
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        #write_dirdata_to_textfile("dirdata.txt", dir(bsObj))
        #content_list = [data for data in bsObj.contents if data != '\t']
        
        print(bsObj.findAll)
        """
        f = open("contents.txt", 'w')
        for content in bsObj.contents:
            
            f.write(content)
            f.write('\n')

        f.close()"""
        
    except AttributeError as e:
        print(e)

if __name__ == '__main__':
    youtube_scrape()