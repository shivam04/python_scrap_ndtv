from bs4 import BeautifulSoup
import gethtml
import json

def getArticleText(web_text):
	# client = MongoClient('mongodb://localhost:27017/')
	# db = client.ndtv
	# cur.execute('''
	# DROP TABLE IF EXISTS News''')

	# cur.execute('''
	# CREATE TABLE News (image TEXT,title TEXT, place TEXT,day TEXT,short_desc TEXT, full_desc TEXT)''')
	#print web_text
	articletext = ""
	soup = BeautifulSoup(web_text)
	article_all = soup.find('div',{'id':'ins_storylist'})
	i = 0
	all_data = list()
	for article in article_all.ul.findAll('li'):
		data = dict()
		try:
			a_tag = article.find('a')
			title = a_tag['title']
			n_url = a_tag['href']
			# print title
			# print n_url
			image_tag = a_tag.find('img')
			#print image_tag
			image = image_tag['src']
			place_date = article.find('div',{'class':'nstory_dateline'})
			kk = place_date.text.split(' | ')[1].split(',')
			day = kk[0]+", "+kk[1]
			place = " ".join(kk[2:])
			short_desc = article.find('div',{'class':'nstory_intro'}).text
			#print title
			# print image
			# print place
			# print day
			# print short_desc
			data['title']=title
			data['image']=image
			data['place']=place
			data['day']=day
			data['short_desc']=short_desc
			print len(short_desc)
			print len(day)
			full =	gethtml.getHtmlText(n_url)
			full_soup = BeautifulSoup(full)
			full_desc = full_soup.find('div',{'id':'ins_storybody'}).text
			#print full_desc
			data['full_desc'] = full_desc
			print len(full_desc)
			print 
			# cur.execute('SELECT title FROM News WHERE title = ? ', (title, ))
			# row = cur.fetchone()
			# if row is None:
			# 	cur.execute('''INSERT INTO News (image, title, place, day, short_desc,full_desc) 
			# 	        VALUES ( ?, ?, ?, ?, ?, ? )''', ( image, title, place, day, short_desc, full_desc, ) )
			# conn.commit()
			#print i
			# ans = db.news.find({"title": title})
			# print ans
			# print "title"
			# result = db.news.insert_one(data)
			# print result.inserted_id
			all_data.append(data)
			# if title not in ans:
			# 	#data = json.dumps(data)
			# 	result = db.news.insert_one(data)
			# i+=1
		except:
			print "except"
			continue
		# db.news.insert_one({'t':'t'})
		# for r_article in article.next_siblings:
		# 	print r_article
	# 		place_date = r_article.find('div',{'class':'nstory_dateline'})
	# 		place,day = place_date.text.split(' | ')
	# 		short_desc = r_article.find('div',{'class':'nstory_intro'}).text
	# 		print title
	# 		print image
	# 		print place
	# 		print day
	# 		print short_desc
	# 		full =	gethtml.getHtmlText(n_url)
	# 		full_soup = BeautifulSoup(full)
	# 		full_desc = full_soup.find('div',{'id':'ins_storybody'}).text
	# 		print full_desc
	# 		cur.execute('SELECT title FROM News WHERE title = ? ', (title, ))
	# 		row = cur.fetchone()
	# 		if row is None:
	# 			cur.execute('''INSERT INTO News (image, title, place, day, short_desc,full_desc) 
	# 			        VALUES ( ?, ?, ?, ?, ?, ? )''', ( image, title, place, day, short_desc, full_desc, ) )
	# conn.commit()
		# break
	return all_data

def getArticle(url):
	htmltext = gethtml.getHtmlText(url)
	return getArticleText(htmltext)

