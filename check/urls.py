from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    #path('', views.req, name='request'),
    #path('detail', views.submit, name='submit'),

    url(r'^$', views.available, name='availability'),
    url(r'^submit/$', views.submita, name='submita'),
]
