from django.conf.urls import url
from django.contrib import admin
from .views import (
    login_view,
    register,
    logout_view
    #ClubListCityAPIView,
    )
urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout_view,name='logout'),
]