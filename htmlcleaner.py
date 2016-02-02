import requests
from bs4 import BeautifulSoup
import re
import sys
import os

import settings


IMPORTANT_TAGS = {
                  'h1' : True,
                  'h2' : True,
                  'p'  : True,
}



EPS = 5

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class HtmlCleaner():
	def __init__(self):
		self.flag = False
		self.html = None
		self.url = None
		self.deep_html_list = []
  

	def get_html(self, url):
		r = requests.get(url)
		html = BeautifulSoup(r.content,"html.parser")
		return html
	
	# Находим наилучшие div'ы
	def find_important_content(self, html):
		for i in range(1, settings.DEEP):
			html = html.findAll("div")
			html = self.find_important_divs(html)
			self.deep_html_list.append(html)
			if self.flag:
				settings.DEEP = i
				return html
		
		return html
  
  # Ищем div'ы с найбольшим количеством тегов указанных  в IMPORTANT_TAGS
	def find_important_divs(self, html):
		max_tags = 0
		index_max = 0
		if not html:
			self.flag = True
			return []
		
		for index, div in enumerate(html):
			tags = div.findAll(IMPORTANT_TAGS)
			if not tags:
				continue
			if max_tags < len(tags):
				max_tags = len(tags)
				index_max = index
		
		if max_tags <= 1:
			self.flag = True
		
		return html[index_max]

  # Форматируем текст
	def formating(self,text):
		if re.match(r'<h[1-9]*',str(text)):
			text = str(text).upper()
			text = text + '\n'
		
		if settings.URL:
			r = re.compile(r'<a.*?href="([^"]+)".*?>')
			href = r.search(str(text))
			if href:
				url = "[%s]" % href.group(1)
				text = re.sub(r'<a.*?href="([^"]+)".*?>',url, str(text))
		
		text = re.sub(r'</li>', '\n', str(text))
		text = re.sub(r'</p>', '\n', str(text))
		text = re.sub(r'\/\*\*[^/]*\/', '', str(text))
		text = re.sub(r'\<[^>]*\>', '', str(text))
		
		return text

  # Определяем из списка найденных данных наилучший
	def check_content_with_tags(self, content):
		deep = 1
		if not self.flag:
			content = self.deep_html_list[-1].findAll(settings.tags_settings)
		else:
			if not content:
				deep += 1
			content = self.deep_html_list[-deep].findAll(settings.tags_settings)
			min_len = len(content)
			while len(content) < min_len + EPS:
				if deep == len(self.deep_html_list):
					break
				content =  self.deep_html_list[-deep].findAll(settings.tags_settings)
				deep += 1
			content =  self.deep_html_list[-deep].findAll(settings.tags_settings)
		
		return content

	def check_content_without_tags(self, content):
		deep = 1
		if not self.flag:
			content = self.deep_html_list[-1].findAll(text=True)
		else:
			if not content:
				deep += 1
			content = self.deep_html_list[-deep].findAll(text=True)
			min_len = len(content)
			while len(content) < min_len + EPS:
				if deep == len(self.deep_html_list):
					break
				content =  self.deep_html_list[-deep].findAll(text=True)
				deep += 1
			content =  self.deep_html_list[-deep].findAll(text=True)
			
		return content

	def cleaning(self,html):
		self.flag = False
		self.deep_html_list = []
		clean_html = []
		content = self.find_important_content(html)
		
		if not settings.TEXT:
			content = self.check_content_with_tags(content)
		else:
			content = self.check_content_without_tags(content)
		
		for  text in content:
			count_char = 0
			if settings.TEXT:
				if len(text) == 1:
					continue
			
			new_text = self.formating(text)
			if len(new_text) > 80:
				new_text = "%s\n" %(new_text)
			for char in new_text:
				if char != '\n':
					count_char += 1
			if count_char == 0:
				continue
			clean_html.append(new_text)
		return clean_html
	

def create_path_from_url(url):
	url_path = url.split('/')
	url_path = '/'.join(url_path[1:])
	path = os.path.join(BASE_DIR, url_path[1:])
	if not os.path.isdir(path):
		os.makedirs(path)
		path = os.path.join(path,"index.txt")
	else:
		path = os.path.join(path,"index.txt")
	return path

def main():
	url = sys.argv[1]
	path = create_path_from_url(url)
	
	site =  HtmlCleaner()
	html = site.get_html(url)
	text = site.cleaning(html)
	
	file = open(path, 'w')
	file.write('\n'.join(text))
	file.close()
	
	print('Очистка завершена.')
	print("Файл находится в %s" %(path))
	print("Настройки по умолчанию:")
	print("DEEP: %s" % str(100))
	print("TEXT: %s" % str(False))
	print(" URL: %s" % str(True))
	print("Возможные способы улучшения результата")
	print("1. Изменяйте значение DEEP от  %s  до 2 в настройках." %(str(settings.DEEP)))
	print("2. Измените значение TEXT на True.")
	print("3. Хотите убрать ссылки. Измените значение URL на False.")


if __name__ == "__main__":
	main()

	