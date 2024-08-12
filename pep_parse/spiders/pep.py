import scrapy
import re
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep = response.css('section#numerical-index td a::attr(href)')
        for pep_url in pep:
            yield response.follow(pep_url,
                                  callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get().replace('-', '')
        number, name = re.search(r'PEP (?P<number>\d+) – (?P<name>.+)',
                                 title).groups()
        status = (
            response.css('dt:contains("Status") + dd').css('abbr::text').get()
        )
        data = {
            'number': number,
            'name': name,
            'status': status,
        }
        yield PepParseItem(data)
