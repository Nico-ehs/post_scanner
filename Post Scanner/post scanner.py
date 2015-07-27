# -*- coding: utf-8 -*-
import requests
url_re=r"""(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))"""
import extract_links
import re
import ast
from operator import itemgetter
import time
import os

class site_data():
    def __init__(self, sitename, site_url, link_extractor):
        self.sitename=sitename
        self.pages=[]
        self.pagelist=[]
        self.link_extractor=link_extractor
        self.unscanned_pages=[site_url]
    def get_links(self,page):
        links=remove_multiple(self.link_extractor(page.text))
        print(page.url)
        return [x for x in links if (x not in (self.pagelist+self.unscanned_pages))]
    def scan_page(self):
        page=requests.get(self.unscanned_pages[0])
        print(page.url)
        self.pages.append(page)
        self.pagelist.append(page.url)
        self.unscanned_pages.extend(self.get_links(page))
        self.unscanned_pages=self.unscanned_pages[1:]
    def full_scan(self):
        print("test1.5")
        while self.unscanned_pages != [] and len(self.pages) <= 6:
            print('pagelist=')
            print(str(self.pagelist))
            print('unsscanned pages=')
            print(str(self.unscanned_pages))
            self.scan_page()
            print('pagelist=')
            print(str(self.pagelist))
            print('unsscanned pages=')
            print(str(self.unscanned_pages))
        print(str(self.unscanned_pages))
    def output(self):
        r=[self.pages]
        return r
    def save_output(self):
        make_site_dir_1(self.sitename)
        for x in self.pages:
            save_page(x.text, x.url, self.sitename)
        path='/site data/'+self.sitename
        save_file('pagelist.txt',str([self.pagelist,self.unscanned_pages]),path)
        get_sitelist()
        return 1
##    def load_data(self):
##        pages=load_site(self.sitename)






def linktest_1(link):
    r=1
    linktest=[]
    linktest+=["https://twigserial.wordpress.com/20" in link]
    linktest+=['#' not in link]
    linktest+=['?' not in link]
    linktest+=[link[-1]==r"/"]
    linktest+=['"' not in link]
    linktest+=['feed' not in link]
    for x in linktest:
        if x==False:
            r=0
    return r

def remove_multiple(list_in):
    r=[]
    for x in list_in:
        if x not in r:
            r.append(x)
    return r

def add_new(list_1,list_2):
    t1=time.time()
    r=list_1
    for x in list_2:
        if x not in r:
            r.append(x)
    t2=time.time()
    print(str(t2-t1))
    return r

def link_fn1(text):
    links=extract_links.extract_m(text)
    vaild_links=[x for x in links if linktest_1(x)==1]
    return vaild_links


def save_file(filename,text,path):
    m_dir=os.getcwd()
    os.chdir(m_dir+path)
    f_out=open(filename, "w")
    out=text
    f_out.write(out)
    f_out.close
    os.chdir(m_dir)
    return True

def load_file(filename,path):
    m_dir=os.getcwd()
    os.chdir(m_dir+path)
    f_in=open(filename, "r").read
    f_out.close
    os.chdir(m_dir)
    return f_in



def make_site_dir_1(sitename):
    m_dir=os.getcwd()
    print(m_dir)
    os.chdir(m_dir+'/site data')
    if sitename not in os.listdir(os.getcwd()):
        os.chdir(m_dir+'/site data')
        os.mkdir(sitename)
        os.chdir(m_dir+'/site data/'+sitename)
        os.mkdir("html data")
    os.chdir(m_dir)
    return 1

def save_page(d,filename,sitename):
    m_dir=os.getcwd()
    os.chdir(m_dir+'/site data/'+sitename+'/html data')
    fn=filename
    fn=fn.replace("/",'')
    fn=fn.replace("\\",'')
    fn=fn.replace(":",'')
    fn=fn.replace("/",'')
    f_out=open(fn+'.html', "w")
    out=str(d)
    f_out.write(out)
    f_out.close
    os.chdir(m_dir)
    return 1
    



def load_page(filename,sitename):
    m_dir=os.getcwd()
    os.chdir(m_dir+'/site data/'+sitename+'/html data')
    f_in=open(filename, "r")
    d_in=f_in.read()
    r=d_in
    os.chdir(m_dir)
    return r




def load_site(sitename):
    m_dir=os.getcwd()
    os.chdir(m_dir+'/'+sitename+'/html data')
    pages=[]
    files=os.listdir(os.getcwd())
    for x in files:
        pages+=[[x,open(x, "r").read()]]        
    os.chdir(m_dir)
    return pages

def get_sitelist():
    m_dir=os.getcwd()
    os.chdir(m_dir+'/site data')
    sitelist=os.listdir(os.getcwd())
    os.chdir(m_dir)
    save_file('sitelist.txt',str(sitelist),'')
    return True


url="https://twigserial.wordpress.com/2014/12/24/taking-root-1-1/"
scan1=site_data('twig', url, link_fn1)
scan1.full_scan()
f_out=open('test.txt', "w", encoding='utf-8')
f_out.write(str(scan1.pagelist))
f_out.close
scan1.save_output()
get_sitelist()






    
# def linktest_2(link):
#     r=1
#     linktest=[]
#     linktest+=["http://slatestarcodex.com/20/" in link]
#     linktest+=['#' not in link]
#     linktest+=['?' not in link]
#     linktest+=[link[-1]==r"/"]
#     linktest+=['"' not in link]
#     linktest+=['feed' not in link]
#     for x in linktest:
#         if x==False:
#             r=0
#     return r

# def link_fn2(text):
#     links=extract_links.extract_m(text)
#     vaild_links=[x for x in links if linktest_2(x)==1]
#     return vaild_links

# url="http://slatestarcodex.com/"
# scan1=site_data('SSC', url, link_fn2)
# scan1.full_scan()
# f_out=open('test.txt', "w")
# f_out.write(str(scan1.pagelist))
# f_out.close
# scan1.save_output()
# get_sitelist()











