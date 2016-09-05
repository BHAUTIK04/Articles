from django.conf.urls import url

from .views import (
    CommentsCreateAPIView
    )

urlpatterns = [
    url(r'^create/(?P<articles_id>[0-9]+)$', CommentsCreateAPIView.as_view(), name='create'),
#     url(r'^edit/(?P<id>[0-9]+)$', ArticleUpdateAPIView.as_view(), name='update'),
#     url(r'^delete/(?P<id>[0-9]+)$', ArticleDeleteAPIView.as_view(), name='delete'),
]
