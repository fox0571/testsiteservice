from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    #path('', views.req, name='request'),
    #path('detail', views.submit, name='submit'),

    url(r'^$', views.req_list, name='list'),
    #url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^new/$', views.req_new, name='req_new'),
    url(r'^submit/$', views.submit, name='submit'),
]
