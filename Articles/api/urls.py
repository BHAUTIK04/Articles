from django.conf.urls import url

from .views import (
    ArticleCreateAPIView,
    ArticleDeleteAPIView,
    ArticleUpdateAPIView,
    )

urlpatterns = [
    url(r'^create/$', ArticleCreateAPIView.as_view(), name='create'),
    url(r'^edit/(?P<id>[0-9]+)$', ArticleUpdateAPIView.as_view(), name='update'),
    url(r'^delete/(?P<id>[0-9]+)$', ArticleDeleteAPIView.as_view(), name='delete'),
]
