from celery import shared_task
from django.http import HttpResponse

from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from backends import settings

@shared_task(bind=True)
def add(self):
    a = 10
    b = 20
    print(a + b)
    return HttpResponse("Done")

@shared_task(bind=True)
def mul(self, x, y, z):
    a = 10
    b = 50
    res = x * y * z
    print(x, y, z)
    print(a * b)
    return res

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "celery mail sending test"
        message      = "You are recieving mail because you subscription is expired"
        to_mail      = user.email
        print(to_mail)
        send_mail(
            subject = mail_subject,
            message = message,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [to_mail],
            fail_silently = True,
        )
    return HttpResponse("Email sent")
    

from backends.celery import app
@app.task
def div(x, y):
    return x / y

