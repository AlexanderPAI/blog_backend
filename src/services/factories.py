import factory


from django.contrib.auth.models import User
from factory.django import DjangoModelFactory

from follows.models import Follow
from posts.models import IsRead, Post


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user%d' % n)
    is_staff = 'True'


class PostFactory(DjangoModelFactory):
    author = factory.SubFactory(UserFactory)

    title = factory.Faker(
        "sentence",
        nb_words=2,
        variable_nb_words=True,
    )
    text = factory.Faker(
        "sentence",
        nb_words=5,
        variable_nb_words=True,
    )

    class Meta:
        model = Post


class IsReadFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)

    class Meta:
        model = IsRead


class FollowFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Follow