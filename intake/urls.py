"""URL Configuration."""

from . import views
from django.conf.urls import url


app_name = 'intake'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_member_signup/$', views.new_member_signup, name="new_member")
]
