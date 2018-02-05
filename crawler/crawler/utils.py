from scrapy.selector import Selector as scp

def to_compose_search_string(artist, music):
	search_string = "'{} {}' site:www.letras.mus.br".format(artist, music)
	return search_string.replace("&","")

def duck_search_string(search_string):
    return "https://duckduckgo.com/?q=" + search_string

def select_lyrics_link(page_source):
    lyrics_link = scp(text=page_source).xpath('//a[@class="result__a"]/@href').extract_first()
    return lyrics_link.replace("traducao.html","")