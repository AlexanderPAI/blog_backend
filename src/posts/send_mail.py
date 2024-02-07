from django.core.mail import send_mail, send_mass_mail

from posts.models import Post


def get_last_posts_feed(user):
    user_email = user.email
    last_posts = Post.objects.filter(author__following__user=user.id)[:5]
    last_posts_str = ''
    for _ in last_posts:
        last_posts_str = last_posts_str + '\n' + _.author.username
        last_posts_str = last_posts_str + '\n' + _.title
        last_posts_str = last_posts_str + '\n' + _.text + '\n'
    return user_email, last_posts_str


def send(user_email, last_posts):
    send_mail(
        subject='Недавние посты',
        message='Недавние посты: \n' + last_posts,
        from_email='ya@ya.ru',
        recipient_list=[user_email],
    )
