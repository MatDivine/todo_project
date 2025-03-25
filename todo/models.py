from django.db import models

# Create your models here.



class Todo(models.Model):
    todo_title = models.CharField(max_length=300)
    todo_content = models.TextField()
    todo_priority = models.IntegerField(default=1)
    todo_is_done = models.BooleanField()
    
    
    def __str__(self):
        return f"{self.todo_title}/ Is done : {self.todo_is_done}"
    
    
    
    class Meta:
        db_table = 'todos'