# coding:utf-8

import os
import time
import logging
import re


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # 寻找ui的组件
from selenium.webdriver.common.by import By  # 选择一种索引方式，如xpath
from selenium.webdriver.support import expected_conditions as EC  # 网页打开后的等待条件类
from selenium.common.exceptions import TimeoutException  # 引入超时错误类
# from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

from taobao_config import *  # 引入配置文件变量
import oracle_connect

# 配置日志文件
file = os.getcwd()
logger = logging.getLogger("DefaultLog")
logger.setLevel(logging.INFO)
fh = logging.FileHandler(file + r"/" + "search_taobao_log.txt", mode="w")  # set write txt path ;parameter(w/a)
ch = logging.StreamHandler()  # set print screen
set_format = r"%(asctime)s___%(funcName)s %(name)s %(levelname)s : %(message)s"
formatter = logging.Formatter(set_format)
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)


# def loding_chrome_browser():
#     try:
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])  # 防止出现‘--ignore-certificate-error’错误
#         browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=options)
#         logger.info("初始化浏览器成功")
#         return browser
#     except:
#         logger.error("初始化浏览器失败")


def loding_browser():
    try:
        browser = webdriver.Ie(executable_path=IE_DRIVER_PATH)
        logger.info("初始化浏览器成功")
        return browser
    except:
        logger.error("初始化浏览器失败")


def NowTime():
    return time.strftime("%Y-%m-%d", time.localtime())



def search(mybrowser, key, save_oracle, num=3):
    try:
        url = "https://www.taobao.com"
        logger.info("开始加载: %s" % url)
        mybrowser.get(url)
        time.sleep(5)
        wait = WebDriverWait(mybrowser, 10)
        in_put = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
        logger.info("发现搜索输入框加载成功")
        button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        logger.info("发现搜索输入框确定按钮加载成功")
        in_put.send_keys(key)
        logger.info("输入搜索关键词：%s" % key)
        button.click()
        total_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        get_product(mybrowser, save_oracle=save_oracle,key=key)

        return total_page.text
    except TimeoutException:
        logger.error("连接超时,尝试第%s次连接失败" % num)
        if num > 0:
            return search(mybrowser=mybrowser, key=key, save_oracle=save_oracle,num=num - 1)
        else:
            logger.error("重新连接失败")


def next_page(mybrowser, pagenum, save_oracle,key, num=5):
    try:
        wait = WebDriverWait(mybrowser, 10)
        in_put = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
        button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        in_put.clear()
        in_put.send_keys(pagenum)
        button.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(pagenum)))
        logger.info("翻页到%s页，加载成功" % pagenum)
        get_product(mybrowser=mybrowser, page=pagenum, save_oracle=save_oracle,key=key)
        return True
    except TimeoutException:
        if num > 0:
            logger.error("翻页到%s页超时，重新加载" % pagenum)
            time.sleep(5)
            return next_page(mybrowser=mybrowser, pagenum=pagenum, save_oracle=save_oracle, key=key)
        else:
            return False


def get_product(mybrowser, save_oracle, key, page=1, marktime = NowTime()):
    wait = WebDriverWait(mybrowser, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist > div > div')))  # ?
    html = mybrowser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    product_list = []
    rank = 1
    for j in items:
        product_attribute_tuple = ()
        # product_attribute = {}
        logger.info("开始获取第%s个商品" % rank)
        sku_id = j.find('.pic-box-inner .pic .pic-link').attr('data-nid')
        sku_url = r'https://detail.tmall.com/item.htm?id=' + sku_id
        img_name = j.find('.pic-box-inner .pic .img').attr('alt')
        img_url = j.find('.pic-box-inner .pic .img').attr('data-src')
        price = j.find('.ctx-box .price').text()
        pay_num = j.find('.ctx-box .deal-cnt').text()
        title = j.find('.ctx-box .title').text()
        shop = j.find('.ctx-box .row-3 .shop .shopname').text()
        location = j.find('.ctx-box .row-3 .location').text()
        # product_attribute = {
        #     "time": marktime,
        #     "page": page,
        #     "rank": rank,
        #     "sku_id": sku_id,
        #     "sku_url": sku_url,
        #     "img_name": img_name,
        #     "img_url": img_url,
        #     "price": price,
        #     "pay_num": pay_num,
        #     "title": title,
        #     "shop": shop,
        #     "location": location
        # }
        product_attribute_tuple = (key, marktime, page, rank, sku_id, sku_url,
                                   img_name, img_url, price, pay_num, title, shop, location)
        product_list.append(product_attribute_tuple)
        rank += 1
    logger.info("第%s页商品信息提取完毕" % page)
    try:
        save_oracle.db_insert(insert_table="TAOBAO_SERACH_KEY",
                              head="(fkey,marktime,page,frank,sku_id,sku_url,img_name,img_url,price,pay_num,title,shop,flocation)",
                              num=13,
                              data=product_list)
        logger.info("%s搜索词的%s页数据数据库储存成功" % (key, page))
    except:
        logger.error("%s搜索词的%s页数据数据库储存失败!!!!!!" % (key, page))




def main():
    keylist = KEYLIST

    for mykey in keylist:
        myoracle = oracle_connect.OracleClass()
        get_browser = loding_browser()
        page = search(mybrowser=get_browser, key=mykey, save_oracle=myoracle)
        page = int(re.compile('(\d+)').search(page).group(0))
        logger.info("搜索关键词成功，总搜索到%s页" % page)
        for i in range(2, page + 1): #for i in range(2, page + 1):
            next_page(mybrowser=get_browser, pagenum=i, save_oracle=myoracle,key=mykey)
            time.sleep(5)
        myoracle.db_commit()
        myoracle.db_disconnect()
        get_browser.close()
        time.sleep(20)

if __name__ == '__main__':
    main()