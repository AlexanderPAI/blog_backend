from rest_framework.viewsets import ModelViewSet

from api.v1.serializers import PostSerializer

from posts.models import Post


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
