#### 来自公众号 : DeveloperPython
![](http://upload-images.jianshu.io/upload_images/4653472-b61ffc02ee6e4db5?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


![](http://upload-images.jianshu.io/upload_images/4653472-361eccdf958c2368?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
# **开头**

这两天后台收到了很多读者发消息说：“看了之前写的关于爬虫的文章之后，自己也想写一个爬虫但不知从何下手”。那么我今天就分享一个简单的案例，和大家一起从零写一个简单的爬虫。

在开始分享之前，我想提一件事情。

我知道，爬虫其实在部分外行人心目中一直是一个低劣或者低俗的人才做的事。那么，不管你是不是这么想，我只能说一句：要是没有爬虫我相信很多公司根本就没法起来。

那么，今天我主要通过一个爬虫框架 Scrapy 来一步步实现爬取 **V2EX** 首页所有的热门文章，旨在让你掌握这个框架来爬取对自己有用的数据。

# **正文**

## ** 一、Scrapy 是什么？**
官网：
http://scrapy-chs.readthedocs.io/zh_CN/latest/intro/overview.html

Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。可以应用到数据挖掘，信息处理或存储历史数据等一系列的程序中。

其最初是为了页面爬取（更确切的来说，网络爬取）所设计的，也可以应用在获取API所返回的数据或者通用的网络爬虫。

Scrapy是一个非常强大且好用的爬虫框架，它不仅提供了一些开箱即用的基础组件，还提供了强大的自定义功能。

框架的学习就是修改配置文件，填充代码就可以了。

## 二、安装 Scrapy？
由于我是用 Mac 来开发的，所以安装命令也是 Mac 下的，至于 Window 和 Linux 可以参考安装。

> pip install scrapy

当然，一开始你得有 Python 的开发环境，这里就不安利 Python 的安装方法了。直接百度即可。

## 三、用 Scrapy 创建一个项目

Scrapy 中提供了 startproject 命令来创建爬虫项目。命令如下：

> scrapy startproject V2EX

我们创建一个项目 V2EX 用来爬取 V2 首页文章的所有信息。
![](http://upload-images.jianshu.io/upload_images/4653472-6d48f6cc7e36a8fa?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
其中：

spiders 文件夹下就是你要实现爬虫功能的核心代码。在 spiders 文件夹下创建一个 spider ，用来爬取 V2 首页文章。

scrapy.cfg 是项目的配置文件。

settings.py用于设置请求的参数，使用代理，爬虫数据后文件保存等等的。

## 四、Scrapy 爬取 V2 首页文章

1、*新建 v2exSpider*

在 spiders 文件夹下新建一个文件， v2exSpider.py
![](http://upload-images.jianshu.io/upload_images/4653472-322e7212457d6053?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

如上图，start_urls 中添加 v2ex 的首页地址，同时重写 parse 方法。这样 Spider 将基于 start_urls 中的地址进行访问，并将数据回调给 parse 方法。

其中，response 就是返回的网页数据。

处理好的数据放在 items 中，在 items.py 设置好要处理哪些数据字段。这里我们来抓取 V2 首页的：作者地址、作者头像、文章地址、所属节点、作者昵称、最后一次回复者昵称、最后一次回复者地址、最后一次回复时间。

那么，要解析处理哪些数据在 items.py 中定义好，也就相当于 java 中的实体类:
![](http://upload-images.jianshu.io/upload_images/4653472-385a128e24900e05?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2、 *分析 V2EX 首页各元素的 xpath*

xpath 的概念可以在 [60行代码拿到10G国外xx视频...](http://mp.weixin.qq.com/s?__biz=MzU3ODAxNDcwNQ==&mid=2247483803&idx=1&sn=8edb2576cb9594913b87de02d2b13e50&chksm=fd7a9d05ca0d1413e372b5ae9912fbf1e3daaeeaa4f23f5810d03f998a3a13fdd9881f64adca&scene=21#wechat_redirect) 中了解，当然你可以直接看这个教程：

http://www.w3school.com.cn/xpath/index.asp

通过 Chrome 打开 v2ex.com ，同时在当前页面空白处点击右键，选中 inspect ，这样就可以看到当前页面的 Elements 。
![](http://upload-images.jianshu.io/upload_images/4653472-36c5ce250f02533d?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
（图片略大，耐心访问）

在这里我们可以分析出来每一篇文章的标题、地址等等的 xpath 路径。

同时，发现首页的50篇文章都是属于 div[@class='cell item'] 的数据，因此我们可以通过 
selector.xpath('//div[@class="cell item"]') 
拿到所有文章的数据，然后再分析出具体数据的 xpath ，从而拿到了所有需要的数据。

解析的数据保存：

![](http://upload-images.jianshu.io/upload_images/4653472-5da4b1f4663e5210?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这时数据分析处理好了，还有最重要的一步，提交：
> yield v2Item

OK！ 万事俱备，数据保存在哪里，什么格式？

在 settings.py 中加入两行代码:

![](http://upload-images.jianshu.io/upload_images/4653472-18d7d82ac1dd7f99?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

如何运行这个爬虫？
scrapy crawl v2exSpider

这样就可以把 V2EX 的首页文章信息都爬取到了本地的 csv 文件中了。

最后，你会发现当前代码只能爬取 V2 中首页的文章，这时候你就需要分析到 v2ex 中下一页的 xpath ，然后拿到这个 url ，通过 yield Request(next_link,callback=self.parse)，这样就可以一直爬取到 v2 最后一页的数据。
来看看数据：
![](http://upload-images.jianshu.io/upload_images/4653472-4dc06822babb8796?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# **总结**

爬虫需谨慎，爬虫需有度。
本篇文章中项目的源代码托管在 Github，点击 【阅读原文】 。
....end...

行为艺术要持之以恒，iOS专用赞赏通道。
![](http://upload-images.jianshu.io/upload_images/4653472-5d4a410f85a0d01b?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

长摁‘识别二维码’，一起进步

![](http://upload-images.jianshu.io/upload_images/4653472-c5b805eacf2780e6?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

生活不止眼前的苟且，还有手下的代码、
和嘴上的扯淡
——
个人博客: http://xiyoumc.0x2048.com
Github:https://www.github.com/xiyouMc
