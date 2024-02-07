from celery_app import app

from django.contrib.auth.models import User

from posts.send_mail import get_last_posts_feed, send


@app.task
def repeat_send_mail():
    users = User.objects.all()
    for user in users:
        user_id = user.id
        user_email, last_posts = get_last_posts_feed(user)
        send(user_email, last_posts)
