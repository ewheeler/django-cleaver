from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

from . import views

urlpatterns = patterns('',
                       url(r'^experiments/$', views.experiments,
                           name='xray_experiments'),
                       url(r'^api/experiments/$',
                           views.experiments_json,
                           name='xray_experiments_json'),
                       )
