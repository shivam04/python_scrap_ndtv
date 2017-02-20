from __future__ import unicode_literals
from mongoengine import *
from django.db import models

# Create your models here.
class NewsNdtv(Document):
	title = StringField(max_length=1000)
	image = StringField(max_length=1000)
	place = StringField(max_length=1000)
	day = StringField(max_length=2000)
	short_desc = StringField(max_length=5000)
	meta = {'allow_inheritance': True}
	def __unicode__(self):
		return self.title
