from django.urls import path
from .views import (
    test,
    send_mail_to_all,
    TodoListView,
    test,
)
urlpatterns = [
    path('test', test, name="test"),
    path('mail', send_mail_to_all, name='mail'),
    path('todos', TodoListView.as_view(), name='todos'),
    path('test', test)
]
