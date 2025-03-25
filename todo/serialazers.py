from rest_framework import serializers
from .models import Todo, user


class TodoSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = ["id", "todo_title", "todo_content", "todo_priority", "todo_is_done"] # same below
        fields = "__all__"
        
        
class UserSerialaizer(serializers.ModelSerializer):
    todos = TodoSerialaizer(read_only = True, many = True)
    
    class Meta:
        model = user
        # fields = ["id", "todo_title", "todo_content", "todo_priority", "todo_is_done"] # same below
        fields = "__all__"