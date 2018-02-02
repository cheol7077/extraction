# -*- coding:utf-8 -*-
import pymysql
import traceback
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

    def selectBoard (self, value):
        try:
            with self.conn.cursor() as cursor:
                sql = '''SELECT id, title, url FROM board WHERE keywords is null AND cid = %s'''
                cursor.execute(sql, (value))
                result = cursor.fetchall()              
        except:
            print('===================except from DB select===================')
            traceback.print_exc()
            result = 'dbError'
        return result
    
    def delete (self, value):
        try:
            with self.conn.cursor() as cursor:
                sql = '''DELETE FROM board where id = %s'''
                result = cursor.execute(sql, (value))
                self.conn.commit()
        except:
            print('===================except from DB select===================')
            traceback.print_exc()
            result = 'dbError'
        return result
    
    def updateKeywords (self, values):
        try:
            sql = '''UPDATE board SET keywords=%s where id=%s'''
            result = self.cursor.execute(sql, values)
            self.conn.commit()                
        except :
            print('update err: ')
            traceback.print_exc()
            result = None            
        return result