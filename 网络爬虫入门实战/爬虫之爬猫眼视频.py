import requests
from lxml import etree
import time
import re
import os

# 获取网页源代码
def get_page(url):
    '''
    查找headers:
    1、打开F12后点击Network后随意登录一个网站
    2、点击官网标志
    3、点击Headers往下便能找到User-Agent
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    html = response.text
    # print(type(html))
    return html


# 解析网页源代码
def parse_page1(html):
    html_elem = etree.HTML(html)
    '''
    etree.HTML()：
    调用HTML类对HTML文本进行初始化，成功构造XPath解析对象，同时可以自动修正HTML文本（标签缺少闭合自动添加上）
    '''
    '''
    快速获取xpath：
    先F12,然后用Ctrl+Shift+C快速选中Web界面的元素，然后在元素上右键-->复制-->复制XPath
    '''
    movies_urls = html_elem.xpath('//h4[@class="video-name one-line"]/a[@href]/@href')
    movies_names = html_elem.xpath('//h4[@class="video-name one-line"]/a[@href]/text()')
    '''
    text()函数
    获取元素文本内容
    '''
    print("----------------------------------------")
    for movies_url, movies_name in zip(movies_urls, movies_names):
        print(movies_url, movies_name)

        # 获取文本
        movie_id_string = requests.get(movies_url).text
        print(movie_id_string)

        # . 表示所有的,但是只匹配一个,除了/n
        # * 表示按照前面的方式进行匹配
        movie_mp4_url = re.search('source src="(.*)" type', movie_id_string).group(1)
        print(movie_mp4_url)

        # 因为视频是二进制文件,所以需要获取content
        mp4 = requests.get(movie_mp4_url).content

        # 写入文件夹
        with open('./movie/%s.mp4' % movies_name, 'wb') as data_file:
            data_file.write(mp4)

    time.sleep(1)


# 开始爬取网页
def crawl():
    url = 'https://www.maoyan.com/news?showTab=3&showTab=3&offset={0}'
    '''
    用Request时对于大部分的页面来说只需要两个参数，一个是url也就是请求的网址，另外一个就是headers，
    而headers中最重要的就是user-agent，其他的参数都没有这两个参数重要。
    所以可以只留下这两个参数再去请求页面，如果请求不下来再去尝试添加其他参数。
    '''
    print('开始爬取')
    os.makedirs("movie")
    for page in range(0, 160, 16):  # 0 25 50 75
        # print('正在爬取第 ' + str(page+1) + ' 页至第 ' + str(page+25) + ' 页......')
        html = get_page(url.format(page))
        data = parse_page1(html)
        time.sleep(1)  # 延迟1秒
    print('结束爬取')


crawl()
