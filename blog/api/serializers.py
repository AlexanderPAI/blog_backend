from rest_framework import serializers

from posts.models import IsRead, Post


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели Post."""
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('__all__')
        read_only_fields = ('author',)
