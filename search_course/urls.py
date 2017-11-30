from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search_page, name='search_page'),
    url(r'^result/$', views.result_page, name='result_page'),
]
