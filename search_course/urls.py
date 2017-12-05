from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='sign_up'),
    url(r'^userPage/$', views.userPage, name='userPage'),
    url(r'^search/$', views.search_page, name='search_page'),
    url(r'^search/result/$', views.result_page, name='result_page'),
]
