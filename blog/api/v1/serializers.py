from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from follows.models import Follow, User
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


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = '__all__'

        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'author'),
            ),
        )

    def validate_author(self, value):
        user = self.context.get('request').user
        if user == value:
            raise serializers.ValidationError(
                'The user cannot subscribe to his blog'
            )
        return value
