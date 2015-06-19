## extract links
import re


def extract_m(text):
    r=[]
    u=[]
    url_re=r"""(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))"""
    urls=re.findall(url_re,text)
    for x in range(len(urls)):
        u=u+[urls[x][0]]
    return u

##
####def test_url1()
##
##files=os.listdir(os.getcwd())
##a=files[1]
##f=open(a)
##b=f.read()
##f.close()
##u=extract_m(b)
