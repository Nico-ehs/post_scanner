## extract text
import os



def get_section(text,start,end):
    r=['']
    r1=text.split(start,1)
    if len(r1)==2:
        r2=r1[1].split(end,1)
    return r

def multi_get_section(text,start,end):
    r=[get_section(text,start,end)]
    if len(r)==3:
        r1=multi_get_section(r[2],start,end)
        r=r+r1
##    if len(r)>1:
##        if len(r[1])==3:
##            r=r[:2]+multi_get_section(r[2],start,end)
    return r

def remove_tags(text):
    r=""""""
    t=0
    for x in range(len(text)):
        if text[x]=='>' or text[x]=='<':
            if text[x]=='>':
                t=0
            if text[x]=='<':
                t=1
        else:
            if t==0:
                r=r+text[x]
    return r


def selection(text,start,end):
    r=''
    r1=text.split(start,1)
    if len(r1)==2:
        r=r1.split(end)[0]
    return r

def multi_selection(text,start,end):
    r1=text.split(start)
    r1=r1[1:]
    r=[]
    for x in range(len(r1)):
        r=r+r1[x].split(end)[0]
    return r
    

def extract_main(text):
    r=[]
    for x in range(len(text)):
        r=[]
    return r


def extract_comments(text):
    r=1
    return r


##files=os.listdir(os.getcwd())
##a=files[1]
##f=open(a)
##t1=f.read()
##f.close()
##s1=[r'article id="post',r'</article><!-- #post-## -->']
##t2=selection(t1,s1[0],s1[1])
##t2='<'+t2
##r=remove_tags(t2)
##
##f=open('test1.txt','w')
##f.write(r)
##f.close
