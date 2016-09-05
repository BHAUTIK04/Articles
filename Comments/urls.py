from django.conf.urls import url, include
from Comments.views import create_view

urlpatterns = [
    url(r'^create/(?P<artid>[0-9]+)$', create_view, name='comment'),
#     url(r'^home/', home_view, name='home'),

]
