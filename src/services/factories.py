import factory
from django.contrib.auth.models import User
from factory.django import DjangoModelFactory

from follows.models import Follow
from posts.models import IsRead, Post


class UserFactory(DjangoModelFactory):
    """Генератор тестовых пользователей."""
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.LazyAttribute(lambda n: '{0}@test.com'.format(n.username).lower())
    is_staff = 'True'


class PostFactory(DjangoModelFactory):
    """Генератор тестовых постов."""
    class Meta:
        model = Post

    author = factory.Iterator(User.objects.all())

    title = factory.Faker(
        "sentence",
        nb_words=2,
        variable_nb_words=True,
    )
    text = factory.Faker(
        "sentence",
        nb_words=10,
        variable_nb_words=True,
    )


class IsReadFactory(DjangoModelFactory):
    """Генератор статутов постов 'Прочитан.'"""
    user = factory.Iterator(User.objects.all())
    post = factory.Iterator(Post.objects.all())

    class Meta:
        model = IsRead


class FollowFactory(DjangoModelFactory):
    """Генератор подписок."""
    user = factory.SubFactory(UserFactory)
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Follow
