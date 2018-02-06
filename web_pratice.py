from bs4 import BeautifulSoup
import python_function_def as fun_self_def
cates = [];
info = [];
with open('C:/Users/Administrator/Desktop/z文件归档/python学习/lesson2/new_index.html','r') as wb_data:
    soup = BeautifulSoup(wb_data,'lxml')
    imags = soup.select('body > div.main-content > ul > li > img')
    titles = soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    descs = soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    rates = soup.select('body > div.main-content > ul > li > div.rate > span')
    lis = soup.select('body > div.main-content > ul > li')
    cate1s = soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info > span:nth-of-type(1)')
    # print(imags,titles,descs,rates,cate1s,cates,sep='\n----------\n')

for li in lis:
    #catelis = li.select('div.article-info > p.meta-info > span')
    catelis = li.find_all('span')
    cates.append(catelis);

for li in lis:
    #find 与 find_all 区别  find只查询一个结果, find_all 查询一个集合
    #print(li.find('span'))
    # print(li.find_all('span'))
    # print(li.find_all(name = 'span',class_ = 'meta-cate'))
    span = li.find_all(name = 'span',class_ = 'meta-cate')[0];
    #parent 迭代出当前节点的父辈节点(上一级别的  父节点同级的所有节点)  parents 向上迭代,迭代到树根为止,将树所有节点迭代完毕
    #print(span.find_parent())
    #print(span.find_parents())


for title,image,desc,rate,cate in zip(titles,imags,descs,rates,cates):
    data = {
        'title':title.get_text(),
        'image':image.get('src'),
        'desc':desc.get_text(),
        'rate':rate.get_text(),
        'cate':fun_self_def.html_attr_trav(2,cate)
    }
    info.append(data)
title_datas = [];
rate_datas = [];
for data in info:
    rate_data = float(data['rate']);
    if rate_data > 3:
        title_datas.append(data['title']);
        rate_datas.append(rate_data)
print(title_datas,rate_datas,'---\n')

