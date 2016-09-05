from rest_framework.permissions import IsAuthenticated
from Articles.models import Articles
from .serializers import (
    ArticleCreateUpdateSerializer,
    ArticleDeleteUpdateSerializer
    )
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from .permissions import IsOwnerOrReadOnly


class ArticleCreateAPIView(CreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class ArticleDeleteAPIView(UpdateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleDeleteUpdateSerializer
    lookup_field = 'id'
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class ArticleUpdateAPIView(UpdateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)