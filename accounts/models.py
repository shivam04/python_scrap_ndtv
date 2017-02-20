from __future__ import unicode_literals
from mongoengine import *
from django.db import models
from mongoengine.context_managers import switch_db
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User)
	# first_name = models.CharField(max_length=50)
	# last_name = models.CharField(max_length=50)
	token = models.CharField(max_length=50)

