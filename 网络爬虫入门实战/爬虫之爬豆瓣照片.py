import requests
from lxml import etree
import time
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
def parse_page1(html, page):
    html_elem = etree.HTML(html)
    result = etree.tostring(html_elem)  # 输出修正后的html
    '''
    etree.HTML()：
    调用HTML类对HTML文本进行初始化，成功构造XPath解析对象，同时可以自动修正HTML文本（标签缺少闭合自动添加上）
    '''
    # pages = html_elem.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div')
    '''
    快速获取xpath：
    先F12,然后用Ctrl+Shift+C快速选中Web界面的元素，然后在元素上右键-->复制-->复制XPath
    '''
    address = html_elem.xpath('//div[@class="pl2"]/a/@href')
    title = html_elem.xpath('//div[@class="pl2"]/a/@title')
    info = html_elem.xpath('//p[@class="pl"]/text()')
    num = html_elem.xpath('//div[@class="star clearfix"]/span[@class="rating_nums"]/text()')
    pic = html_elem.xpath('//a[@class="nbg"]/img/@src')
    '''
    text()函数
    获取元素文本内容
    '''
    os.makedirs("books")
    for j in range(0, 25):
        print(pic[j])
        with open('books\\' + str((page * 25) + j + 1) + '.jpg', 'wb') as fp:
            pi = requests.get(pic[j])
            fp.write(pi.content)
            print("保存第%d本书成功" % int((page * 25) + j + 1))

    time.sleep(1)  # 延迟1秒


# 开始爬取网页
def crawl():
    url = 'https://book.douban.com/top250?start={0}'
    '''
    用Request时对于大部分的页面来说只需要两个参数，一个是url也就是请求的网址，另外一个就是headers，
    而headers中最重要的就是user-agent，其他的参数都没有这两个参数重要。
    所以可以只留下这两个参数再去请求页面，如果请求不下来再去尝试添加其他参数。
    '''
    print('开始爬取')
    for page in range(0, 110, 10):  # 0 25 50 7 5
        # print('正在爬取第 ' + str(page+1) + ' 页至第 ' + str(page+25) + ' 页......')
        html = get_page(url.format(page))

        data = parse_page1(html, page)
        time.sleep(1)  # 延迟1秒
    print('结束爬取')


crawl()
