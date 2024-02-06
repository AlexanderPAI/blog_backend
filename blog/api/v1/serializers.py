from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор модели Post."""
    author = serializers.StringRelatedField()
    is_read = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author',)

    def get_is_read(self, obj):
        """Метод для отображения поля поста 'Прочитано'."""
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        if obj.is_read.filter(user=user):
            return True
        return False
