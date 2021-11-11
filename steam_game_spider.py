import re
import time
import scrapy
import argparse
from scrapy.crawler import CrawlerProcess
from export_data import save_data, clean_text, real_time


def clear_percentage(string):
    pattern = r'%'
    clear_percent = re.sub(pattern, '', string)
    result = re.sub(',', '.', clear_percent)

    return float(result)


class SteamSpider(scrapy.Spider):
    name = 'steam_games_spider '

    def start_requests(self):
        list_page_number = range(3, 4) # DEBUG
        # list_page_number = range(1, 4354)
        urls = [*map(lambda page: f'https://store.steampowered.com/search/?sort_by=Price_ASC&page={page}',
                list_page_number)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sel_games = response.xpath(
            '//div[@id="search_results"]/div[@id="search_result_container"]/div[@id="search_resultsRows"]/a')
        data = sel_games.extract()
        for game in sel_games:

            list_name = game.xpath(
                './/div[@class="col search_name ellipsis"]/span/text()').extract()
            name = clean_text(list_name[-1])

            list_release_date = game.xpath(
                './/div[@class="col search_released responsive_secondrow"]/text()').extract()
            if len(list_release_date) == 0:
                release_date = ''
            else:
                release_date = clean_text(list_release_date[-1])

            list_discount = game.xpath(
                './/div[@class="col search_discount responsive_secondrow"]/span/text()').extract()
            if len(list_discount) == 0:
                discount = 0
            else:
                discount = clear_percentage(list_discount[-1])

            list_price = game.xpath(
                './/div[@class="col search_price  responsive_secondrow"]/text()').extract()
            # get free game
            if len(list_price) == 0:
                list_price = game.xpath(
                    './/div[@class="col search_price discounted responsive_secondrow"]/text()').extract()
            price = clean_text(list_price[-1])

            list_link = game.xpath('./@href').extract()
            link = clean_text(list_link[-1])
            # print(f'{name} ({release_date})  - {price} - {discount} - {link}') # DEBUG
            data = (name, release_date, price, discount, link)
            if discount == -100:
                list_sale_free.append(data)
            list_data.append(data)
        print()


if __name__ == '__main__':
    list_data = []
    list_sale_free = []
    parser = argparse.ArgumentParser(
        description='Get all steam games', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s', '--save', help='save as csv or excel file',
                        type=str, choices=['csv', 'excel','all'], default=None)
    args = parser.parse_args()
    # running spider
    start_time = time.time()
    process = CrawlerProcess()
    process.crawl(SteamSpider)
    process.start()
    print(f'Total: {len(list_data)} games')

    # save to  file
    save_type = args.save
    header = ['Name', 'Release date', 'Price', 'Discount', 'Link']
    save_data(list_data=list_data, save_type=save_type,
              header=header, file_name='list_steam_games')
    end_time = time = time.time()
    print('Elapsed:', real_time(end_time - start_time))
    print('Sale free game: ',list_sale_free)
