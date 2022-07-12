from rest_framework import serializers

from social.models.post import Post


class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = ('id','body','image','created_on','author','likes','dislikes')





