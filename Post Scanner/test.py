import os


# def save_file(filename,text,path):
#     m_dir=os.getcwd()
#     os.chdir(m_dir+path)
#     f_out=open(filename, "w", encoding='utf-8')
#     f_out.write(text)
#     f_out.close
#     os.chdir(m_dir)
#     return True


def load_file(filename,path):
    m_dir=os.getcwd()
    os.chdir(m_dir+path)
    f_in=open(filename, "r", encoding='utf-8').read()
    os.chdir(m_dir)
    return f_in
    
    
# def get_sitelist():
#     m_dir=os.getcwd()
#     os.chdir(m_dir+'/site data')
#     sitelist=os.listdir(os.getcwd())
#     os.chdir(m_dir)
#     return sitelist
    
# def posts_test(site):
#     m_dir=os.getcwd()
#     os.chdir(m_dir+'/site data/'+sitename)
#     posts=load_file("",posts.txt)
    
    
def name_test(sitename):
    m_dir=os.getcwd()
    # os.chdir(m_dir+'/site data/'+sitename)
    comments=eval(load_file("comments.txt",'/site data/'+sitename))
    names=list(map((lambda x: x[3]),comments))
    for x in names[:100]:
        print(x)
    return 1
    
def post_test(sitename):
    m_dir=os.getcwd()
    # os.chdir(m_dir+'/site data/'+sitename)
    posts=eval(load_file("posts.txt",'/site data/'+sitename))
    names=list(map((lambda x: x[2]),posts))
    for x in names:
        print(x)
    return 1
        
# name_test("twig")
post_test("ESR")

    

