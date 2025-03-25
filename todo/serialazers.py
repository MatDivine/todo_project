from rest_framework import serializers
from .models import Todo


class TodoSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = ["id", "todo_title", "todo_content", "todo_priority", "todo_is_done"] # same below
        fields = "__all__"