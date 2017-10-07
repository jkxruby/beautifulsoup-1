from bs4 import BeautifulSoup

with open('/Users/jkxuan/Desktop/1_2answer_of_homework/1_2_homework_required/index.html', 'r', encoding="gb2312") as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    scores = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    stars = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')

   # print(images, prices, scores, stars, sep= '\n---------\n')


for image, price, score, star in zip (images,prices,scores,stars):
    data = {
        'image':image.get('src'),
        'price':price.get_text(),
        'score':score.get_text(),
        'star':len(star.find_all("span", class_='glyphicon glyphicon-star'))
    }

    print(data)






#     titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a') # 复制每个元素的css selector 路径即可
#     images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
#     reviews = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
#     prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
#     stars = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
#     # 为了从父节点开始取,此处保留:nth-of-type(2),观察网页,多取几个星星的selector,就发现规律了





'''

          body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > img    图片地址
价格       body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.caption > h4.pull-right
评分数     body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p.pull-right
星数       body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p:nth-child(2) > span:nth-child(3)
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(2) > div > div.ratings > p:nth-child(2)
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(4) > div > div.ratings > p:nth-child(2) > span:nth-child(3)
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(8) > div > div.ratings > p:nth-child(2) > span:nth-child(4)

'''




















































# from bs4 import BeautifulSoup
# path = './1_2_homework_required/index.html'  #这里使用了相对路径,只要你本地有这个文件就能打开
#
# with open(path, 'r') as wb_data: # 使用with open打开本地文件
#     soup = BeautifulSoup(wb_data, 'lxml') # 解析网页内容
#     # print(wb_data)
#
#     titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a') # 复制每个元素的css selector 路径即可
#     images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
#     reviews = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
#     prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
#     stars = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
#     # 为了从父节点开始取,此处保留:nth-of-type(2),观察网页,多取几个星星的selector,就发现规律了
#
# # print(titles,images,rates,prices,stars,sep='\n--------\n')  # 打印每个元素,其中sep='\n--------\n'是为了在不同元素之间添加分割线
#
# for title, image, review, price, star in zip(titles, images, reviews, prices, stars):  # 使用for循环,把每个元素装到字典中
#     data = {
#         'title': title.get_text(), # 使用get_text()方法取出文本
#         'image': image.get('src'), # 使用get 方法取出带有src的图片链接
#         'review': review.get_text(),
#         'price': price.get_text(),
#         'star': len(star.find_all("span", class_='glyphicon glyphicon-star'))
#         # 观察发现,每一个星星会有一次<span class="glyphicon glyphicon-star"></span>,所以我们统计有多少次,就知道有多少个星星了;
#         # 使用find_all 统计有几处是★的样式,第一个参数定位标签名,第二个参数定位css 样式,具体可以参考BeautifulSoup 文档示例http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#find-all;
#         # 由于find_all()返回的结果是列表,我们再使用len()方法去计算列表中的元素个数,也就是星星的数量
#     }
#     print(data)
