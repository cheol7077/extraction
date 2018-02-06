# -*- coding:utf-8 -*-
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import word2vec
import pymysql


def connect():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='hubhub',
                           db='community',
                           charset='utf8mb4')
    
    return conn


def wordLearing(cur, date):
    sql = '''SELECT keywords
                FROM board
                WHERE date_format(date, '%%Y-%%m-%%d') = %s'''
    
    cur.execute(sql, (date))
    keys = []
    for row in cur.fetchall():
        #print(row)
        if row[0] is not None:
            words = row[0].split(' ')
            keys.append(words)
    model = word2vec.Word2Vec(keys, size=200, window=10, hs=1, min_count=2, sg=1)
    print(model.most_similar(positive=['문재인'], topn=10))


if __name__ == '__main__':
    conn = connect()
    cur = conn.cursor()
    date = '2018-01-31'
    
    wordLearing(cur, date)
    
    conn.close()
