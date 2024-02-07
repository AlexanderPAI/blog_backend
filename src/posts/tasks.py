from celery_app import app

from posts.send_mail import send

@app.task
def repeat_send_mail():
    send('ya@bob.ru')
