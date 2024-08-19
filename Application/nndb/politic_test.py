import json
import csv
import pandas as pd




with open('D:\\PythonProject\\MyPython\\ch01basic\\정치_naver_news.json', 'r', encoding='utf-8') as f1:
    json_politics_news = json.load(f1)

with open('D:\\PythonProject\\MyPython\\ch01basic\\경제_naver_news.json', 'r', encoding='utf-8') as f2:
    json_economys_news = json.load(f2)

with open('D:\\PythonProject\\MyPython\\ch01basic\\스포츠_naver_news.json', 'r', encoding='utf-8') as f3:
    json_sports_news = json.load(f3)

with open('D:\\PythonProject\\MyPython\\ch01basic\\it_naver_news.json', 'r', encoding='utf-8') as f4:
    json_its_news = json.load(f4)

with open('D:\\PythonProject\\MyPython\\ch01basic\\연애_naver_news.json', 'r', encoding='utf-8') as f5:
    json_entertaiments_news = json.load(f5)

# print(json.dumps(json_news, indent=4, sort_keys= True, ensure_ascii=False))

count = 0
cnt = 0
naver_news = []
news_data = [
    (json_politics_news, '정치'),
    (json_economys_news, '경제'),
    (json_sports_news, '스포츠'),
    (json_its_news, 'IT'),
    (json_entertaiments_news, '연애')
]

for news_list, section in news_data:
    for news in news_list:
        cnt += 1
        count += 1
        title = news['title']
        link = news['link']
        pDate = news['pDate']
        description = news['description']
        naver_news.append([count,title,section,link,pDate,description])
        if cnt == 100:
            cnt = 0
            break

print(json.dumps(naver_news, indent=4, ensure_ascii=False))

newsFrame = pd.DataFrame(naver_news)
newsFrame.columns = ['count', 'title', 'section', 'link', 'pDate', 'description']
newsFrame.head()

filename ='naver_news.csv'
newsFrame.to_csv(filename, encoding='utf-8-sig', index=False)
