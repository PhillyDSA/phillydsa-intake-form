# -*- coding: utf-8 -*-
"""URL Configuration."""

from intake import views
from django.conf.urls import url


app_name = 'intake'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^confirm/(?P<pk>[0-9]+)/$', views.NewMemberUpdate.as_view(), name="confirm"),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.EventPersonDetailView.as_view(), name="detail")
]
