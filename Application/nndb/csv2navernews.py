import sqlite3
import pandas as pd

csv_file = './data/navernews.csv'
df = pd.read_csv(csv_file)

conn = sqlite3.connect('./../mydatabase.sqlite3')
cursor = conn.cursor()

sql = '''
create table nNews(
count integer primary key autoincrement,
title text,
section text,
link text,
pDate real,
description text,
img_link text,
text text
)
'''

cursor.execute(sql)

df.to_sql('nNews', conn, if_exists='append', index=False)

conn.commit()
conn.close()

print('데이터 베이스 파일에 데이터 추가를 성공하였습니다.')