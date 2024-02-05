from rest_framework.viewsets import ModelViewSet

from api.serializers import PostSerializer

from posts.models import IsRead, Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
