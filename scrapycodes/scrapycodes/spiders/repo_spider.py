import scrapy

class RepoSpider(scrapy.Spider):
    name = 'GitHubScrapy'
    start_urls = ['https://github.com/search?q=scrapy&type=Repositories/']

    def parse(self, response):
        for link in response.css('a.v-align-middle::attr(href)'):
            yield response.follow(link.get(), callback = self.parse_repo)

        for n in range(2, 10):
            next_page = f'https://github.com/search?p={n}&q=scrapy&type=Repositories/'
            yield response.follow(next_page, callback = self.parse)
    

    def parse_repo(self, response): 
        yield{
            'about': response.css('p.f4::text').get().strip() if response.css('p.f4::text').get() != None else None,
            'stars': ''.join(filter(str.isdecimal, response.css('a.Link--muted strong')[0].get())),
            'watching': ''.join(filter(str.isdecimal, response.css('a.Link--muted strong')[1].get())),
            'forks': ''.join(filter(str.isdecimal, response.css('a.Link--muted strong')[2].get())),
        }
'''

response.css('a.v-align-middle::attr(href)').get()

response.css('p.f4::text').get().strip()#about
response.xpath('//*[@id="repo-content-pjax-container"]/div/div/div[3]/div[2]/div/div[1]/div/div[2]/a/strong').get()[8:9]#stars
response.xpath('//*[@id="repo-content-pjax-container"]/div/div/div[3]/div[2]/div/div[1]/div/div[3]/a/strong').get()[8:9]#Watchers
            'stars': response.xpath('//*[@id="repo-content-pjax-container"]/div/div/div[3]/div[2]/div/div[1]/div/div[2]/a/strong').get()[8:9],
            'watching': response.xpath('//*[@id="repo-content-pjax-container"]/div/div/div[3]/div[2]/div/div[1]/div/div[3]/a/strong').get()[8:9]'''