#!/usr/bin/env python  
# encoding: utf-8  


from django.conf.urls import url
from art.views  import InterfaceHandler
from art.index_handler import IndexHandler
from art.search_handler import SearchHandler
from art.detail_handler import DetailHandler
from art.statistic_handler import LinesHandler, HistogramHandler, ArtListHandler, ArtEditGetHandler, ArtEditPostHandler
from art.views import render_index
from django.views.generic.base import RedirectView
from art.views import TestPostHandler, GetArtsHandler
from art.views import add_handler


urlpatterns = [
    url(r'^interface/', InterfaceHandler),
    url(r'^test_post/', TestPostHandler),
    url(r'^add',add_handler),
    url(r'^get_arts', GetArtsHandler),

    #the front web site
    url(r'^index', IndexHandler),
    url(r'^search', SearchHandler),
    url(r'^detail', DetailHandler),

    #the statistic web site.
    url(r'^shtml', render_index),
    url(r'^art_list', ArtListHandler),
    url(r'^art_edit', ArtEditGetHandler),
    url(r'^art_ed_post', ArtEditPostHandler),
    url(r'^line', LinesHandler),
    url(r'^statics/', RedirectView.as_view(url='/art/histogram')),
    url(r'^histogram/', HistogramHandler),
]
