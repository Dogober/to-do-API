from rest_framework import serializers

from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "title", "description", "due_date", "status")
