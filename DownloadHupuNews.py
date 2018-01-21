import urllib.request
import re
import ssl

#全局取消证书验证，避免SSL: CERTIFICATE_VERIFY_FAILED
ssl._create_default_https_context = ssl._create_unverified_context

#将爬虫伪装为浏览器
headers=("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36 QQBrowser/4.2.4718.400")

#创建一个openner对象
opener = urllib.request.build_opener()

#为opener添加header
opener.addheaders = [headers]

#将opener添加为全局
urllib.request.install_opener(opener)
data=urllib.request.urlopen("https://nba.hupu.com").read().decode("utf-8")

#使用正则表达式进行匹配，并将匹配到的新闻网址放入一个list
pat = 'href="(https://bbs.hupu.com/.*?)"' 
mydata = re.compile(pat).findall(data)

for i in range(0,len(mydata)):
    print("第" + str(i+1 )+"次爬取")

    #使用urlretrieve将新闻直接下载到本地
    file = "/Users/Rocky1/Desktop/hupu/" + str(i) + ".html"
    urllib.request.urlretrieve(mydata[i],file)
    
    print("------success-------")
