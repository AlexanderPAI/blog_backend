from django.core.mail import send_mail

from posts.models import Post


def get_last_posts():
    last_posts = Post.objects.all()[:5]
    last_posts_str = ''
    for _ in last_posts:
        last_posts_str = last_posts_str + '\n' + _.author.username
        last_posts_str = last_posts_str + '\n' + _.title
        last_posts_str = last_posts_str + '\n' + _.text
    return last_posts_str


def send(user_email):
    last_posts = get_last_posts()
    send_mail(
        subject='Недавние посты',
        message=last_posts,
        from_email='ya@ya.ru',
        recipient_list=[user_email],
    )
