from rest_framework import serializers
from email_send_app.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Todo
        fields = "__all__"