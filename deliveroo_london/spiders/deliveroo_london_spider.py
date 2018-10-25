# -*- coding: utf-8 -*-
import scrapy
import datetime
import csv


class DeliverooLondonSpiderSpider(scrapy.Spider):
    name = 'deliveroo_london_spider'
    allowed_domains = ['deliveroo.co.uk']
    start_urls = ['https://deliveroo.co.uk/sitemap']

    def parse(self, response):
        links = response.xpath('//*[@class="no-ui mbottom50"]/ul//ul//a//@href').extract()
        self.log(f'There are: {len(links)} links')
        for link in links:
            url = f'https://deliveroo.co.uk{link}'
            yield scrapy.Request(url=url, callback=self.menu_parse)

    def menu_parse(self, response):
        url = response.url
        name = response.xpath('//*[@class="restaurant__name"]//text()').extract_first()
        name = name.split(' - ')
        if len(name) != 1:
            name = ' '.join(name[:-1])
        else:
            name = name[0]
        rating = response.xpath('//*[@class="restaurant__rating ratings"]//text()').extract_first()
        price = response.xpath('//*[@class="price-category"]//text()').extract_first()
        tags = response.xpath('//*[@class="restaurant__metadata-tags"]/small/text()').extract()
        address = response.xpath('//*[@class="address"]//text()').extract_first()
        address_split = address.split(', ')
        phone = response.xpath('//*[@class="phone"]//text()').extract_first()
        date_accessed = datetime.datetime.now()
        street = ', '.join(address_split[:-2])
        postcode = address_split[-1]
        city = address_split[-2]

        with open('data.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                [
                    url,
                    date_accessed,
                    city,
                    name,
                    rating,
                    address,
                    street,
                    postcode,
                    phone,
                    price
                ] + tags
            )
