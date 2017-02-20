from django.conf.urls import url
from django.contrib import admin
from .views import (
    NewsList,
    #ClubListCityAPIView,
    )
urlpatterns = [
    url(r'^$', NewsList.as_view(), name='list'),
]