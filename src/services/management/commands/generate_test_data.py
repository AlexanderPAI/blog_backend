import random
from django.db import transaction
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from follows.models import Follow
from posts.models import IsRead, Post

from services.factories import UserFactory, PostFactory, IsReadFactory, FollowFactory

NUM_USERS = 100
NUM_FOLLOWS = 500
NUM_POSTS = 10000
NUM_ISREAD = 1000


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        models = [User, Post, Follow, IsRead]
        for m in models:
            m.objects.all().delete()

        for _ in range(NUM_FOLLOWS):
            follow = FollowFactory()
            print(follow.user.username, follow.author.username)

        # for _ in range(NUM_USERS):
        #     user = UserFactory()
        #     print(user.username)

        for _ in range(NUM_POSTS):
            post = PostFactory()
            print(post.title)



        for _ in range(NUM_ISREAD):
            isread = IsReadFactory()
            print(isread.user.username, isread.post.title)
