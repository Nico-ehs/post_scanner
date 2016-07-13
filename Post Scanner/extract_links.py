## extract links
# -*- coding: utf-8 -*-
import re


def extract_m(text):
    # r=[]
    # u=[]
    # f_out=open('test.txt', "w", encoding='utf-8')
    # f_out.write(text)
    # url_re=r"""(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))"""
    url_re='<a href="?\'?([^"\'>]*)'
    urls=re.findall(url_re,text)
    # print(len(urls))
    # print("test3")
    # print(str(urls)[0:200])
    # for x in range(len(urls)):
    #     u=u+[urls[x][0]]
    return urls

##
####def test_url1()
##
##files=os.listdir(os.getcwd())
##a=files[1]
##f=open(a)
##b=f.read()
##f.close()
##u=extract_m(b)
