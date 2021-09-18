from bs4 import BeautifulSoup
import cloudscraper 

def match_class(target):
	def do_match(tag):
		classes = tag.get('class', [])
		return all(c in classes for c in target)
	return do_match

def stats(ign: str):
	url = 'https://play.esea.net/index.php?s=search&query=' + ign

	scraper = cloudscraper.create_scraper()
	page = scraper.get(url).content
	soup = BeautifulSoup(page, "html.parser")
	results = soup.find_all('a')
	i = 0
	for link in results:
		sub = str(link.get('href'))[0:7]
		if (sub == '/users/'):
			return 'https://play.esea.net/users/' + str(link.get('href')).split('/')[2]