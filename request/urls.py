from django.urls import path

from . import views

urlpatterns = [
    path('', views.req, name='request'),
    path('', views.submit, name='submit'),
]
