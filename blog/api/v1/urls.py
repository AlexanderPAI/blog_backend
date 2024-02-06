from django.urls import include, path
from rest_framework import routers

from api.v1.views import FollowViewSet, PostViewSet


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('follows', FollowViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
