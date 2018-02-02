# -*- coding:utf-8 -*-
import pymysql

class connDB:    
    def __init__(self):  
        self.conn = pymysql.connect(host='localhost',
                    user = 'root',
                    password = 'hubhub',
                    db='community',
                    charset='utf8mb4')
        self.cursor = self.conn.cursor()
        
    def __del__(self): #객체 소멸시 하는일
        self.cursor.close()
        self.conn.close()
        print('DB connection is closed')
        
    def selectBoard(self):
        sql = '''SELECT keywords
                    FROM board'''
        
        self.cursor.execute(sql)
        
        return self.cursor.fetchall()

    def selectNumberDate(self):
        sql = '''SELECT date_format(date, "%Y-%m-%d"), count(*)
                    FROM board
                    GROUP BY day(date)'''
        
        self.cursor.execute(sql)
        
        return self.cursor.fetchall()
    
    def selectNumberPosts(self):
        sql = '''SELECT count(*)
                    FROM board'''
        
        self.cursor.execute(sql)
        
        return self.cursor.fetchone()
    
    def selectAmountDay(self, value):
        sql = '''SELECT count(*)
                    FROM board
                    WHERE date_format(date, '%%Y-%%m-%%d') = %s'''
        
        self.cursor.execute(sql, (value))
        
        return self.cursor.fetchall()
    
    def selectWordDay(self, value):
        sql = '''SELECT keywords
                    FROM board
                    WHERE date_format(date, '%%Y-%%m-%%d') = %s'''
        
        self.cursor.execute(sql, (value))
        
        return self.cursor.fetchall()