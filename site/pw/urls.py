from coltrane.urls import urlpatterns as base_urlpatterns

from django.urls import path

from .feeds import ContentFeed

urlpatterns = [
    path("rss.xml", ContentFeed()),
] + base_urlpatterns
