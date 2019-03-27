from bs4 import BeautifulSoup
import urllib.request
import ast
import re


#출력 파일명
OUTPUT_FILE_NAME = 'output.txt'

URL = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=021&aid=0002385984'

def get_text(url):
    source_code_from_url = urllib.request.urlopen(url)
    soup = BeautifulSoup(source_code_from_url,'lxml',from_encoding='utf-8')
    text=''
    for item in soup.find_all('div',id='articleBodyContents'):
        text = text + str(item.find_all(text=True))
    return text

def main():
    with open(OUTPUT_FILE_NAME,'w') as file:
        result_text = get_text(URL)
        file.write(result_text)

if __name__ =='__main__':
    main()
    