import mechanize


def getHtmlText(url):
	br = mechanize.Browser()
	br.set_proxies({"http": "ipg_2014082:8960709251@192.168.1.107:3128",
                })
	br.add_proxy_password("ipg_2014082", "8960709251")
	htmltext = br.open(url).read()
	return htmltext


def getHtmlFile(url):
	br = mechanize.Browser()
	htmlfile = br.open(url)
	return htmlfile