import mechanize


def getHtmlText(url):
	br = mechanize.Browser()
	htmltext = br.open(url).read()
	return htmltext


def getHtmlFile(url):
	br = mechanize.Browser()
	htmlfile = br.open(url)
	return htmlfile