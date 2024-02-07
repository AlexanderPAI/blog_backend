from django.shortcuts import get_object_or_404

from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers import FollowSerializer, PostSerializer
from posts.models import IsRead, Post


class PostViewSet(ModelViewSet):
    """Представление для постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(
        methods=['post', 'delete'],
        detail=True
    )
    def is_read(self, request, pk):
        """
        Эндпоинт posts/{id}/is_read -
        изменить статус прочитан/не прочитан.
        """
        user = request.user
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST':
            if IsRead.objects.filter(user=user, post=post).exists():
                return Response(
                    {f'Пост {post.title}': 'уже был отмечен прочитанным ранее'}
                )
            IsRead.objects.create(user=user, post=post)
            return Response(
                {f'Пост: {post.title}': 'отмечен прочитаным'}
            )

        if request.method == 'DELETE':
            is_read = get_object_or_404(IsRead, user=user, post=post)
            is_read.delete()
            return Response(status=204)
        return Response(status=405)


class FollowViewSet(ModelViewSet):
    """Представление для подписок."""
    serializer_class = FollowSerializer
    pagination_class = None

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
