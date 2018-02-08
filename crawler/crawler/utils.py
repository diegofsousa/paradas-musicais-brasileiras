from scrapy.selector import Selector as scp
import requests as req
from requests.exceptions import RequestException
import json

def to_compose_search_string(artist, music):
	search_string = "'{} {}' site:www.letras.mus.br".format(artist, music)
	return search_string.replace("&","")

def duck_search_string(search_string):
	return "https://duckduckgo.com/?q=" + search_string

def select_lyrics_link(page_source):
	try:
		lyrics_link = scp(text=page_source).xpath('//a[@class="result__a"]/@href').extract_first()
		return lyrics_link.replace("traducao.html","")
	except Exception as e:
		return None

def work_in_request_url(url):
	try:
		request = req.get(url)
		if request.status_code == 200:
			print("  Ok!")
			return request.content
		print(" Not status 200, trying again...")
		return None
	except RequestException as e:
		print(" "+e)
		try:
			request = req.get(url)
			if request.status_code == 200:
				print("  Ok!")
				return request.content
			print(" Not status 200")
			return None
		except RequestException as e:
			print(" "+e)

def select_lyric_in_html(page_source):
	lyric = scp(text=page_source).xpath('//div[@class="cnt-letra p402_premium"]/article/p/text()').extract()
	return list(set(' '.join(lyric).lower().split(' ')))

def select_number_views(page_source):
	number_views = scp(text=page_source).xpath('//div[@class="cnt-info_exib"]/b/text()').extract_first()
	return int(number_views.replace('.',''))

def select_gender(page_source):
	return scp(text=page_source).xpath('//div[@id="breadcrumb"]/span/a/span/text()').extract()[1]

def select_music_cipher_url(page_source):
	left_links = scp(text=page_source).xpath('//div[@class="letra-menu"]/a/@href').extract()
	if left_links[0] == "#":
		return left_links[1]
	return left_links[2]

def select_music_chords(page_source):
	page_chords = scp(text=page_source).xpath('//div[@id="js-view-script"]/script/text()').extract()[1]
	try:
		home = page_chords.find('chords: ') + 8
		end = page_chords.find('}]);') - 14
		chords = page_chords[home:end]
		js = json.loads(chords)
		return [chord['chord'] for chord in js]
	except Exception as e:
		return []
	
