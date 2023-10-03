from django.conf.urls import patterns, include, url

from .views import Lookup

urlpatterns = patterns('',
    url(r'^lookup$', Lookup.as_view(), name='geocoder-lookup'),
)
