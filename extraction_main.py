# -*- coding:utf-8 -*-
import connDB
from communityText import c1, c2, c3, c4, c5
from time import ctime, sleep, time
from multiprocessing import Pool, TimeoutError
from konlpy.tag import Twitter

sites = ('fmkorea', 'ppomppu', 'humoruniv', 'ruliweb', 'mlbpark')
cid = {'fmkorea':'c1', 'ppomppu':'c2', 'humoruniv':'c3', 'ruliweb':'c4', 'mlbpark':'c5'}


def noun(text):
    twitter = Twitter()
    result = ''
    
    malist = twitter.pos(text)
    
    for i, word in enumerate(malist):
        if word[1] == 'Noun':
            if i != len(malist) - 1:
                result += word[0] + ' '
            else:
                result += word[0]
    
    return result


def extraction(site):
    start_time = time()
    
    keywords(cid[site])
    
    end_time = time()
    print('실행시간: {}'.format(end_time - start_time))
    
    return site


def keywords(cid):
    print('{} keywords start!'.format(cid))
    db = connDB.connDB()
    deleteSuccess = 0
    deleteFail = 0
    updateSuccess = 0
    updateFail = 0
    total = 0
    
    board = db.selectBoard(cid)
    
    for post in board:
        try:
            total += 1
            titlewords = noun(post[1]) 
            words = noun(eval(cid)(post[2]))
            
            if words is not None:
                keys = titlewords + ' ' + words
                values = (keys, int(post[0]))
                result = db.updateKeywords(values)
                if result != 0:
                    updateSuccess += 1
                else:
                    updateFail += 1
            else:
                result = db.delete(post[0])
                if result != 0:
                    deleteSuccess += 1
                else:
                    deleteFail += 1
            
            sleep(1)
        except Exception as e:
            print(post)
            print(e)
            result = db.delete(post[0])
            if result != 0:
                deleteSuccess += 1
            else:
                deleteFail += 1
            continue
    
    print('exit {} keywords!'.format(cid))
    print('delete - success: {}, fail: {}'.format(deleteSuccess, deleteFail))
    print('update - success: {}, fail: {}'.format(updateSuccess, updateFail))
    print('total: {} cases'.format(total))
    print('=================================')


if __name__ == "__main__":
    with Pool(processes=len(sites)) as process:
        fsites = [process.apply_async(extraction, (site,)) for site in sites]
        
        for fsite in fsites:
            try:
                print('finish ' + fsite.get(timeout=7200) + ' : ', ctime())
            except TimeoutError:
                print ('Failed at:', fsite.get())
                continue
    
    process.close()
    process.join()
