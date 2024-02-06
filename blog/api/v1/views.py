from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers import FollowSerializer, PostSerializer
from posts.models import Post


class PostViewSet(ModelViewSet):
    """Представление для постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(ModelViewSet):
    """Представление для подписок."""
    serializer_class = FollowSerializer

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FeedViewSet(ModelViewSet):
    """Представление для ленты новостей."""
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Post.objects.filter(author__following__user=self.request.user)
