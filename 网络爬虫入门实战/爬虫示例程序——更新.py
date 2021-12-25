import requests
from lxml import etree
import time


# 获取网页源代码

def get_page(url):
    '''
    查找headers:
    1、打开F12后点击Network后随意登录一个网站
    2、点击官网标志
    3、点击Headers往下便能找到User-Agent
    '''
    headers = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    html = response.text
    print(type(html))
    return html


# 解析网页源代码
def parse_page1(html):
    html_elem = etree.HTML(html)
    '''
    etree.HTML()：
    调用HTML类对HTML文本进行初始化，成功构造XPath解析对象，同时可以自动修正HTML文本（标签缺少闭合自动添加上）
    '''
    pages = html_elem.xpath('//*[@id="content"]/div/div[1]/ol/li')
    '''
    快速获取xpath：
    先F12,然后用Ctrl+Shift+C快速选中Web界面的元素，然后在元素上右键-->复制-->复制XPath
    '''
    for i in pages:
        titles = i.xpath('./div/div[2]/div[1]/a/span[1]/text()')
        infos = i.xpath('./div/div[2]/div[2]/p[1]/text()')
        scores = i.xpath('./div/div[2]/div[2]/div/span[2]/text()')
        '''
        text()函数
        获取元素文本内容
        '''
        print("----------------------------------------")
        print("电影名：", titles[0], '\n', "详情：", infos[1].strip(), '\n', "评分：", scores[0] + '分', '\n')
        time.sleep(1)


# 开始爬取网页
def crawl():
    url = 'https://movie.douban.com/top250?start={0}&filter='
    '''
    用Request时对于大部分的页面来说只需要两个参数，一个是url也就是请求的网址，另外一个就是headers，
    而headers中最重要的就是user-agent，其他的参数都没有这两个参数重要。
    所以可以只留下这两个参数再去请求页面，如果请求不下来再去尝试添加其他参数。
    '''
    print('开始爬取')
    # for page in range(0,250,25):  # 0 25 50 75
    for page in range(0, 25):  # 0 25 50 75
        # print('正在爬取第 ' + str(page+1) + ' 页至第 ' + str(page+25) + ' 页......')
        html = get_page(url.format(page))
        data = parse_page1(html)
        time.sleep(1)  # 延迟1秒
    print('结束爬取')


crawl()
