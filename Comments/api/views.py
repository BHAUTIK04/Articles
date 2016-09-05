from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from .serializers import CommentCreateSerializer
from Comments.models import Comment
from Articles.models import Articles

class CommentsCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]
    
        
    def perform_create(self, serializer):
        print serializer
        serializer.save(user=self.request.user)
    