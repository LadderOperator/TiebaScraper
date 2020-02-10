# TiebaScraper（百度贴吧刮削器）

## 简介

一个人畜无害的小爬虫，基于手机网页端的百度贴吧爬取。
~~这是我拿来做贴吧监视的。~~

## 依赖

+ Python3
+ requests
+ BeautifulSoup4

## 功能

有且仅有：
+ 梳理指定第n篇帖子开始的一页（30篇）帖子的标题（含帖子类型）、作者、帖子链接

## 缺陷

包括但不限于：
+ 无法获取置顶帖作者
+ 无法获取帖子发布时间
+ 暂未加入异常处理

## 展望

鬼知道什么时候才会写完：
+ 理论上还可以进一步完善获取最后回复时间以及回复数
+ 已完成的功能都可以归入第一层爬取，根据各帖子的详情能补充作者和发布信息作为第二层爬取（比如加个深入模式啥的）

## 注意

天杀的百度造成了以下问题：
+ 帖子类型花里胡哨，不排除出现例外情况
+ 百度奇葩的昵称制度导致很多账号名字是无法正确识别的