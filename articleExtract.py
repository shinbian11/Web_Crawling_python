import os,re,usecsv #usecsv.py도 있어야 함
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs


#find_all : tag를 추출
#get : tag안의 속성 값을 추출

#--------------------------------------

os.chdir(r'C:\Users\PC1\.spyder-py3')
news = 'https://media.daum.net/'

#마법의 명령어
soup = bs(ur.urlopen(news).read(),'html.parser')  
#ur.urlopen(news).read()로 news URL 불러내고, 그 링크에 있는 내용을 parser를 이용해서 parse 하기 쉽도록 변환하여
#soup라는 곳에 저장함

#soup 에 있는 div 태그 중에서, class 가 cont_thumb인 부분의 text 부분만 출력
for i in soup.find_all('div',{"class": "cont_thumb"}):
    print(i.text) #기사 제목과 출처만 추출
    
print('----------------------------')

#soup 에 있는 a 태그 중, 처음부터 5개만 가져와서, 그 a 태그의 href 속성값 (URL) 만 출력
for i in soup.find_all('a')[:5]:
    print(i.get('href'))
    
print('----------------------------')

print('<header news href list>\n')
for i in soup.find_all('div',{"class": "item_issue"}):
    #soup 에 있는 div 태그의 class가 item_issue 인것만 가져와서, 
    #그 안에 있는 여러 개의 a 태그 중 첫번째 a 태그 안에 있는 href 속성 값(URL)만을 출력
    print(i.find_all('a')[0].get('href'))
    
print('----------------------------')

#--------------------------------------
#기사 본문 내용 추출

article1 = 'https://news.v.daum.net/v/20210618144259405'
soup2 = bs(ur.urlopen(article1).read(),'html.parser')

for i in soup2.find_all('p'):
    print(i.text)

#--------------------------------------
#기사 제목/본문 추출
headline = soup.find_all('div',{"class" : "item_issue"})

for i in headline:
    print(i.text,'\n')
    soup3 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(),'html.parser')
    for j in soup3.find_all('p'):
        print(j.text)

#--------------------------------------
#daum 뉴스 header 기사 4개의 하이퍼링크만 추출

f= open('links.txt','w') # 'links.txt"라는 제목의 쓰기 전용 파일을 만든다.  

# URL 주소 txt 파일로 저장
for i in soup.find_all('div',{"class":"item_issue"}):
    f.write(i.find_all('a')[0].get('href')+'\n' )
f.close()

#--------------------------------------
#article 본문을 txt 파일로 저장

article2 = 'https://news.v.daum.net/v/20210618142647851'
soup3 = bs(ur.urlopen(article2).read(),'html.parser')
f = open('article.txt','w',encoding='UTF-8')
for i in soup3.find_all('p'):
    f.write(i.text)
    print(i.text)
    
f.close()


#--------------------------------------
#daum 뉴스 header 기사 4개의 제목,하이퍼링크,본문 내용을 txt 파일로 저장

soup4 = bs(ur.urlopen('https://news.daum.net/').read(),'html.parser')
f = open('article_total.txt','w',encoding='UTF-8')
 
for i in soup4.find_all('div',{'class' : 'item_issue'}):
    try:
        f.write(i.text+'\n')
        f.write(i.find_all('a')[0].get('href')+'\n')
        soup_small = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(),'html.parser')
        for j in soup_small.find_all('p'):
            f.write(j.text)
    except:
        pass

f.close()



