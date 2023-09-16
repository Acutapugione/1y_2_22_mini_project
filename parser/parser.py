from .parser import ParserSettings
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from typing import List, Dict


class Parser:
    def __init__(self, settings: ParserSettings):
        assert settings, "settings must be not None"
        assert isinstance(
            settings, ParserSettings
        ), f"settings must be instance of {type(ParserSettings)}"

        self.settings = settings
        self.data = None
        self.links = []
        
    def __init_data(self) -> None:
        with urlopen(self.settings.url + self.settings.postfix_url) as r:
            self.data = bs(r.read(), "html.parser")
    
    def __init_links(self) -> None:
        a_tags = self.data.select(self.settings.header_selector)
        self.links = [
            {
                "link" : x.get("href"),
                "header": x.text,
            } 
            for x in a_tags
        ]
        
    def __get_data_from(self, link) -> Dict:
        url = self.settings.url + link if not link.startswith('http') else link
        with urlopen(url) as r:
            data = bs(r.read(), "html.parser")
        text_block = data.select(self.settings.text_selector)
        article = '\n'.join([x.text for x in text_block])
        return article
    
    def parse(self) -> List[Dict]:
        self.__init_data()
        self.__init_links()
        for link in self.links:
            link.upgrade({ 'article': self.__get_data_from(link.get('link'))})
        return self.links