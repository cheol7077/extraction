from keywords.hotKeyword import getPx, getPy, getPxy, getIxy, getWordAvg, getResultDic
import keywords.dbForKey

db = keywords.dbForKey.connDB()
np = db.selectNumberPosts()[0]
px_dic = getPx(np)
py_dic = getPy(np)
pxy_dic = getPxy(np, px_dic, py_dic)
ixy_dic = getIxy(px_dic, py_dic, pxy_dic)
word_avg = getWordAvg(ixy_dic)
result_dic = getResultDic(ixy_dic, word_avg)

for date in result_dic:
    print(date)
    for word in result_dic[date]:
        if word[1] > 0:
            print(word)