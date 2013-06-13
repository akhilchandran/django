from django.conf.urls.defaults import *
from students.views import main_page, details, view, sort_age, sort_mark, remove_details, search

urlpatterns = patterns('',('^$', main_page),('^details$', details),('^view$',view),('^sort_age$', sort_age),('^sort_mark$', sort_mark),('^remove$', remove_details),('^search$', search),)
