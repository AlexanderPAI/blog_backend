from django.urls import include, path
from rest_framework import routers

from api.v1.views import FeedViewSet, FollowViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('follows', FollowViewSet, basename='follows')
router.register('feed', FeedViewSet, basename='feed')


urlpatterns = [
    path('', include(router.urls)),
]
