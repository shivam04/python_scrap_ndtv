from django.shortcuts import render,redirect
from mongoengine import *
from .models import NewsNdtv
import articletext
from rest_framework.test import RequestsClient,APIRequestFactory
from django.http import HttpResponse , HttpResponseRedirect , Http404
from accounts.models import Profile
import json
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

def news_json(request,key=None):
	error = ""
	print request.user
	if not request.user:
		print "login"
		return redirect('/accounts/login/')
	elif key == None:
		print "key"
		return redirect('/accounts/login/')
	else:
		profile = Profile.objects.filter(token=key).first()
		if profile is None:
			error = "Wrong Key"
			return render(request,"ff.html",{'error':error})
		else:
			host =  request.META['HTTP_HOST'] 
			url =  'http://'+host+'/api/?format=json'
			client = RequestsClient()
			data = client.get(url).json()
			return render(request,"ff.html",{'s':data})
def news_xml(request,key=None):
	error = ""
	if not request.user:
		return redirect('/accounts/login/')
	elif key == None:
		return redirect('/accounts/login/')
	else:
		profile = Profile.objects.filter(token=key).first()
		if profile is None:
			error = "Wrong Key"
			return render(request,"ff.html",{'error':error})
		else:
			host =  request.META['HTTP_HOST'] 
			url =  'http://'+host+'/api/?format=xml'
			client = RequestsClient()
			data = client.get(url)
			return render(request,"ff.html",{'s':data})