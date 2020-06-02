# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:32:50 2020

@author: LadderOperator

"""

import requests
from bs4 import BeautifulSoup

mobile_header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0; \
            Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/80.0.3987.87 \
            Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;\
            q=0.9,image/webp,image/apng,*/*;\
            q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }

post_type ={
        "ti_icon_zhiding":"置顶",
        "ti_icon_jing":"精华",
        "ti_icon_yuyin":"语音"
        }

def extract_info(posts:list, ignore_top:bool = True)->dict:
    
    posts_info = []
    
    for post in posts:
        
        post_info = {}
        
        post_title = post.find(attrs={"class":"ti_title"})
        if len(post_title.find_all("span"))>1 and 'class' in post_title.span.attrs:
            post_info["type"] = post_type[post_title.span["class"][-1]]
            if ignore_top == True and post_info["type"] == "置顶":
                continue
        else:
            post_info["type"] = "普通"
        
        post_info["title"] = list(post_title.strings)[-1]
        if post_info["title"].strip() == "":
            post_info["title"] = "[无标题帖子]"
        
        post_author = post.find(attrs={"class":"ti_author_time"})
        
        if post_author == None:
            post_info["author"] = "[未识别作者]"
        else:
            post_author_name = post_author["data-url"].replace("/home/main?un=","")
            if len(post_author_name) == 0:
                post_author_name = post_author.find(attrs={"class":"ti_author"}).text
            post_info["author"] = requests.utils.unquote(post_author_name.strip())
        
        post_info["link"] =  "http://tieba.baidu.com/p/%s" % post["data-tid"]
        
        posts_info.append(post_info)
    
    return posts_info
        
        


def get_posts(tbname:str, pn:int, sort_by_reply:bool = True, ignore_top:bool = True)->dict:
    
    url = "http://tieba.baidu.com/f?kw=%s&pn%s" % (tbname, pn)
    webpage = requests.get(url, headers = mobile_header)
    processed_page = BeautifulSoup(webpage.text, 'lxml')
    tdict = {"class":["tl_top scale-1px-bottom","tl_shadow tl_shadow_new"]}
    post_list = processed_page.find_all(attrs=tdict)
    posts = extract_info(post_list, ignore_top)
    
    return posts