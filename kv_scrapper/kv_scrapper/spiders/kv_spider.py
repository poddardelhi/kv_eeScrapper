import scrapy
from ..items import KvScrapperItem

class KvSpiderSpider(scrapy.Spider):
    name = 'kv_spider'
    page_number =2
    start_urls = [
    'https://www.kv.ee/?act=search.simple&last_deal_type=1&company_id=&page=1&orderby=ob&page_size=100&deal_type=1&dt_select=1&county=1&search_type=new&parish=1061&city%5B%5D=1001&city%5B%5D=5701&city%5B%5D=1003&city%5B%5D=1004&city%5B%5D=1006&city%5B%5D=1007&city%5B%5D=1008&city%5B%5D=1010&city%5B%5D=1011&city%5B%5D=5700&rooms_min=&rooms_max=&price_min=&price_max=&nr_of_people=&area_min=&area_max=&floor_min=&floor_max=&energy_certs=&keyword=%3E']
    
    def parse(self, response):
        last_page= int(response.css(".count::text")[0].extract())
        items = KvScrapperItem()
        for row in response.xpath('//*[@class="object-list-table"]//tbody/tr'):
            name= row.css('.text-truncate a::text').extract()
            link=row.css('.text-truncate a::attr(href)').extract()
            rooms= row.css('.object-rooms::text').extract()
            area= row.css('.object-m2::text').extract()
            price =row.css('.object-price-value::text').extract()
            price_sqm= row.css('.object-m2-price::text').extract()
            description= row.css('.object-excerpt::text').extract()
            items['name']= name
            items['description']=description
            items['link']= link
            items['no_rooms']=rooms
            items['area']=area
            items['price']=price
            items['per_m_sq']=price_sqm
            yield items

        next_page='https://www.kv.ee/?act=search.simple&last_deal_type=1&company_id=&page='+str(KvSpiderSpider.page_number)+'&orderby=ob&page_size=100&deal_type=1&dt_select=1&county=1&search_type=new&parish=1061&city%5B%5D=1001&city%5B%5D=5701&city%5B%5D=1003&city%5B%5D=1004&city%5B%5D=1006&city%5B%5D=1007&city%5B%5D=1008&city%5B%5D=1010&city%5B%5D=1011&city%5B%5D=5700&rooms_min=&rooms_max=&price_min=&price_max=&nr_of_people=&area_min=&area_max=&floor_min=&floor_max=&energy_certs=&keyword=%3E'       
       
        if (int(KvSpiderSpider.page_number)<=last_page):
            KvSpiderSpider.page_number=+1
            yield response.follow(next_page, callback=self.parse)

        
      
        
