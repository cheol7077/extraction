# -*- coding:utf-8 -*-
import math
import keywords.dbForKey
import keywords.abbreviationFile

db = keywords.dbForKey.connDB()
af = keywords.abbreviationFile.abbreviationFile()


def wordCount():
    word_total = {}
    
    boardList = db.selectBoard()
    
    for row in boardList:
        if row[0] is not None:
            words = row[0].split(' ')
            for word in words:
                if word != '' and not (word in af.abbreviation[0]):
                    if not (word in word_total):
                        word_total[word] = 0
                    word_total[word] += 1
    
    keys = sorted(word_total.items(), key=lambda x:x[1], reverse=True)
    
    return keys


def theWordOfTheDay(day, px_dic):
    word_day = {}
    
    dateBoard = db.selectWordDay(day)
    
    for row in dateBoard:
        if row[0] is not None:
            words = row[0].split(' ')
            for word in words:
                if word != '':
                    if word in px_dic:
                        if word in word_day:
                            word_day[word] += 1
                        else:
                            word_day[word] = 1
    
    return word_day


def getPx(np):
    px_dic = {}
    keys = wordCount()
    
    for word, count in keys[:70]:
        px_dic[word] = count / np
    
    return px_dic


def getPy(np):
    py_dic = {}
    
    nd = db.selectNumberDate()
    
    for day in nd:
        aod = db.selectAmountDay(day[0])
        for count in aod:
            py_dic[day[0]] = count[0] / np
    
    return py_dic


def getPxy(np, px_dic, py_dic):
    pxy_dic = {}
   
    for day in py_dic:     
        wtList = theWordOfTheDay(day, px_dic)
        wtList = sorted(wtList.items(), key=lambda x:x[1], reverse=True)   
        word_dic = {}
        for wt in wtList:
            word_dic[wt[0]] = wt[1] / np
        pxy_dic[day] = word_dic
        
    return pxy_dic


def getIxy(px_dic, py_dic, pxy_dic):
    ixy_dic = {}

    for date in pxy_dic:
        ixy_val = {}
        for word in pxy_dic[date]:
            ixy_val[word] = math.log10(pxy_dic[date][word] / (py_dic[date] * px_dic[word]))
        ixy_dic[date] = ixy_val
    
    return ixy_dic


def getWordAvg(ixy_dic):
    word_avg = {}
    
    '''
    for word in px_dic:
        cnt = 0
        total = 0
        for date in ixy_dic:
            if word in ixy_dic[date]:
                cnt += 1
                total += ixy_dic[date][word]
        word_avg[word] = total/cnt
    '''
    
    for date in ixy_dic:
        cnt = 0
        total = 0
        for word in ixy_dic[date]:
            cnt += 1
            total += ixy_dic[date][word]
        if cnt != 0:
            word_avg[date] = total / cnt
    
    return word_avg


def getResultDic(ixy_dic, word_avg):
    result_dic = {}
    result_val = {}
    
    for date in ixy_dic:
        result_val = {}
        for word in ixy_dic[date]:
            result_val[word] = ixy_dic[date][word] - word_avg[date]
        
        result_val = sorted(result_val.items(), key=lambda x:x[1], reverse=True)
        result_dic[date] = result_val
        
    return result_dic


'''
if __name__ == '__main__':
    word_avg = {}
    result_dic = {}
    result_val = {}
    
    np = db.selectNumberPosts()[0]
    px_dic = getPx(np)
    py_dic = getPy(np)
    pxy_dic = getPxy(np, py_dic)
    ixy_dic = getIxy(px_dic, py_dic, pxy_dic)
    word_avg = getWordAvg(ixy_dic)
    result_dic = getResultDic(ixy_dic)
    
    for date in result_dic:
        print(date)
        for word in result_dic[date]:
            if word[1] > 0:
                print(word)
'''
