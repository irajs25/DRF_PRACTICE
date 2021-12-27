from django.shortcuts import render

from email_send_app.mixins import TodoMixin
from .tasks import add, mul, send_mail_func, div
from django.http import HttpResponse

from email_send_app.models import Todo
from email_send_app.serializers import TodoSerializer
from rest_framework import generics
# from django.utils.decorators import method_decorator
from email_send_app.middlewares import my_middleware
# Create your views here.

def test(request):
    add.delay()
    mul.delay(1, 27, 3)
    div.delay(4,2)
    return HttpResponse("Done")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Mail sent")

class TodoListView(TodoMixin):
    pass

# @method_decorator(my_middleware)
@my_middleware
def test(request):
    print("How are You?")
    return HttpResponse("Working this page")