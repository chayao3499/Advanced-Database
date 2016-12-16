import jieba
import codecs
with open('d:/xinwen.txt', 'r') as f:
    for line in f:
        seg = jieba.cut(line.strip(), cut_all = False)
        s= '/'.join(seg)
        m=list(s)
        with open('d:/1.txt','a+')as f:
            for word in m:
                f.write(word.encode('utf-8'))
                #print word