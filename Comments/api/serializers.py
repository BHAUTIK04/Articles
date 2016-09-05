from rest_framework.serializers import ModelSerializer
from Comments.models import Comment

class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["articles","comment_text"]
