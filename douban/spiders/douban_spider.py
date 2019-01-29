# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

# scrapy startproject douban 创建项目
class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名字
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口url
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movieList = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for item in movieList:
            doubanItem = DoubanItem()
            doubanItem['serial_number'] = item.xpath(".//div[@class='item']//em[1]/text()").extract_first()
            doubanItem['movie_name'] = item.xpath(".//div[@class='info']//span[@class='title']/text()").extract_first()
            introduceList = item.xpath(".//div[@class='bd']/p[1]/text()").extract()
            tar = ""
            for introduce in introduceList:
                content = "".join(introduce.split())
                tar += (content + " ")
            doubanItem['introduce'] = tar

            doubanItem['star'] = item.xpath(".//div[@class='star']//span[@class='rating_num']/text()").extract_first()
            doubanItem['evaluate'] = item.xpath(".//div[@class='star']/span[4]/text()").extract_first()
            doubanItem['describe'] = item.xpath(".//div[@class='bd']//span[@class='inq']/text()").extract_first()
            #print(doubanItem)
            yield doubanItem

        nextLink = response.xpath("//span[@class='next']/link/@href").extract()
        if nextLink:
            nextLink = nextLink[0]
            yield scrapy.Request("https://movie.douban.com/top250" + nextLink, callback=self.parse)

