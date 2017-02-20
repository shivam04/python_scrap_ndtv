from django.shortcuts import render
from mongoengine import *
from .models import NewsNdtv
import articletext
# Create your views here.
def scrap(request):
	entry = ""
	for i in range(1,15):
		url ="http://www.ndtv.com/world-news/page-"+str(i) 
		articles = list()
		articles = articletext.getArticle(url)
		if len(articles)>0:
			print "Entry Done Of page "+str(i)+" Of world news"
			for article in articles:
				news = NewsNdtv(title=article['title'],image=article['image'],
					place=article['place'],day=article['day'],
					short_desc=article['short_desc'])
				news.save()
				print news.title
			entry = "done"
		else:
			print "Error"
	news = NewsNdtv.objects.all().first()
	entry = news.title
	print entry
	return render(request,'index.html',{'entry':entry})