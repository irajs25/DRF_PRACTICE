from email_send_app import serializers
from email_send_app.models import Todo
from email_send_app.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response


class TodoMixin(generics.ListAPIView):
    queryset          = Todo.objects.all()
    serializer_class  = TodoSerializer
    permission_classes= (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        todos      = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response({"msg":"Hey There!!!", "data": serializer.data})