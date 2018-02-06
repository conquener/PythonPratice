from bs4 import BeautifulSoup;
import re;
data_info = [];
counts_stars = [];
#查询所有五星的商品
with open("C:/Users/Administrator/Desktop/z文件归档/python学习/week1/1_2/1_2answer_of_homework/1_2_homework_required/index.html",'r') as web_file:
    soup = BeautifulSoup(web_file,'lxml')
    images = soup.select("body > div > div > div.col-md-9 > div > div > div > img");
    titles = soup.select("body > div > div > div.col-md-9 > div > div > div > div > h4 > a");
    prices = soup.select("body > div > div > div.col-md-9 > div > div > div > div > h4.pull-right");
    counts = soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right");
    stars = soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)");
    # print(images,titles,prices,counts,stars,sep="--\n")

for star in  stars:
    counts_star = star.find_all("span",class_="glyphicon glyphicon-star");
    counts_stars.append(counts_star);

for image,title,price,count,counts_star in zip(images,titles,prices,counts,counts_stars):
    data = {
        'image':image.get('src'),
        'title':title.get_text(),
        'price':price.get_text(),
        'count':re.sub('\D','',count.get_text()),
        'count_star':len(counts_star)
    }
    data_info.append(data);

for var in data_info:
    if var['count_star'] > 4 and float(var['count'])>30:
        print(var['title'])