import os

class site_parser():
    def __init__(self,sitename,fn_s_post,fn_s_commets):
        self.sitename=sitename
        self.fn_s_post=fn_s_post
        self.fn_s_commets=fn_s_commets
        self.posts=[]
        self.comments=[]
        self.pagelist=[]
    def scan_page(self,text):
        post=entry_parser(get_post(text),self.fn_s_post,post_data).output
        post[0]=[self.sitename]+post[0]
        new_comments=entry_parser(get_comments(text),self.fn_s_commets,comment_data).output
        # print(str(new_comments)[:50])
        for x in range(len(new_comments)):
            new_comments[x]=[self.sitename,post[0][2]]+new_comments[x]
        # print(str(new_comments)[:50])
        self.posts+=post
        print(len(self.posts))
        self.comments+=new_comments
        print(len(self.comments))
        return 1
    def load_pagelist(self):
        m_dir=os.getcwd()
        os.chdir(m_dir+'/site data/'+self.sitename+'/html data')
        self.pagelist=os.listdir(os.getcwd())
        os.chdir(m_dir)
        return 1
    def full_scan(self):
        self.load_pagelist()
        m_dir=os.getcwd()
        for x in self.pagelist:
            page=load_file(x,'/site data/'+self.sitename+'/html data')
            self.scan_page(page)
        self.save_data()
        return 1
    def save_data(self):
        save_file("posts.txt",str(self.posts),'/site data/'+self.sitename)
        save_file("comments.txt",str(self.comments),'/site data/'+self.sitename)
        return 1

def multi_selection(text,start,end):
    r1=text.split(start)
    r1=r1[1:]
    r=[]
    for x in range(len(r1)):
        r=r+[r1[x].split(end)[0]]
    return r
    
def selection(text,start,end):
    r=''
    r1=text.split(start,1)
    if len(r1)==2:
        r=r1[1].split(end)[0]
    else:
        r=""
    return r





def remove_tags(text):
    for x in range(len(text)):
        if text[x]=='>' or text[x]=='<':
            if text[x]=='>':
                t=0
            if text[x]=='<':
                t=1
            break
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




class entry_parser():
    def __init__(self,data,fn_s,entry_class):
        self.entries=[]
        self.output=[]
        for x in data:
            self.entries+=[entry_class(x,fn_s)]
            self.output+=[self.entries[-1].output()]


class post_data():
    def __init__(self,data,fn_s):
        self.title=fn_s[0](data)
        self.html_id=fn_s[1](data)
        self.date=fn_s[2](data)
        self.author=fn_s[3](data)
        self.text=fn_s[4](data)
    def output(self):
        r=[self.html_id,self.title,self.author,self.date,self.text]
        return r


class comment_data():
    def __init__(self,data,fn_s):
        self.author=fn_s[0](data).replace('\n','').replace('\t','')
        self.date=fn_s[1](data)
        self.depth=fn_s[2](data)
        self.text=fn_s[3](data)
        self.html_id=fn_s[4](data)
    def output(self):
        r=[self.html_id,self.author,self.date,self.depth,self.text]
        return r

    
##site=[[url,linktest_1],[fn_2,[get_fn1(e1[0],e1[1]),get_fn1(e2[0],e2[1]),get_fn1(e3[0],e3[1]),get_fn1(e4[0],e4[1])]]]


def get_post(text):
    r=1
    s='<article id="post'
    e='</article><!-- #post-## -->'
    r=selection(text,s,e)
    return [r]

def get_comments(text):
    r=1
    s='<li class="comment'
    e='<div class="reply">'
    r=multi_selection(text,s,e)
    return r


def selection_fn_gen(s,e):
    r = lambda x: remove_tags(selection(x,s,e))
    return r

def no_tags_selection_fn_gen(s,e):
    r = lambda x: remove_tags(selection(x,s,e))
    return r

def double_selection_fn_gen(s1,e1,s2,e2):
    r = lambda x: selection(selection(x,s1,e1),s2,e2)
    return r


# def format_name_ers(fn)
#     r = lambda x: selection(selection(x,s1,e1),s2,e2)
#     return r

def save_file(filename,text,path):
    m_dir=os.getcwd()
    os.chdir(m_dir+path)
    f_out=open(filename, "w", encoding='utf-8')
    f_out.write(text)
    f_out.close
    os.chdir(m_dir)
    return True


def load_file(filename,path):
    m_dir=os.getcwd()
    os.chdir(m_dir+path)
    f_in=open(filename, "r", encoding='utf-8').read()
    os.chdir(m_dir)
    return f_in


def remove_extra_pages():
    



# comments

# fn1 authour
fn1=no_tags_selection_fn_gen('<div class="comment-author vcard">',
                             '<span class="comment-meta commentmetadata">')
# fn2 date
fn2=double_selection_fn_gen('<span class="comment-meta commentmetadata">',
                            '</time>',
                            'datetime="',
                            '">')
# fn3 depth
fn3=double_selection_fn_gen('depth',
                            'id="li-comment',
                            '-',
                            ' ')
    
# fn4 text
fn4=no_tags_selection_fn_gen('<div class="comment-content">',
                             '</div>')
# fn5 html id
fn5=selection_fn_gen('<article id="comment-',
                     '" class="comment">')
# post 

# fn6 title
fn6=selection_fn_gen('<h1 class="entry-title">',
                     '</h1>')
# fn7 html id
fn7=selection_fn_gen('-',
                     '" class="post-')

# fn8 published_time
fn8=selection_fn_gen('class="entry-date" datetime="',
                     '" pubdate')

# fn9 author
fn9=no_tags_selection_fn_gen('<span class="author vcard">',
                             '</span>')
# fn10 text
fn10=no_tags_selection_fn_gen('<div class="entry-content">',
                              '</div><!-- .entry-content -->')

wordpress_functions_post_1=[fn6,
                                fn7,
                                fn8,
                                fn9,
                                fn10]
wordpress_functions_comments_1=[fn1,
                                fn2,
                                fn3,
                                fn4,
                                fn5]

fns_1=wordpress_functions_comments_1
fns_2=wordpress_functions_post_1

# t1=open("Taking Root 1.1 _ Twig.htm", "r", encoding='utf-8').read()
# t2=entry_parser(get_comments(t1),fns_1,comment)
# print(t2.output[5])
# open("comment_test1.html", "w", encoding='utf-8').write(str(t2.output))
# open("post_test1.html", "w", encoding='utf-8').write(str(post(get_post(t1),fns_2).output()))






# def esr_funtions:
parser=site_parser("twig",fns_2,fns_1)
parser.full_scan()


fns_1[0]=no_tags_selection_fn_gen('<div class="comment-author vcard">',
                             '</span> on')
                             
fns_1[1]=selection_fn_gen('<time pubdate datetime="', '">')
                        
parser=site_parser("ESR",fns_2,fns_1)
parser.full_scan()

