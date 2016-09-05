from django.conf.urls import url, include
from .views import create_view, home_view, detail_view, update_view, delete_view

urlpatterns = [
    url(r'^$', home_view, name="home"),
    
    url(r'^create/', create_view, name='create'),
    url(r'^details/(?P<art_number>[0-9]+)$', detail_view, name='detail'),
    url(r'^edit/(?P<art_number>[0-9]+)$', update_view, name='update'),
    url(r'^delete/(?P<art_number>[0-9]+)$', delete_view, name='delete'),
]
