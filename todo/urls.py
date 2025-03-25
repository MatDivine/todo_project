from django.urls import path
from . import views


urlpatterns = [
    path('',view=views.all_todos),
    path('<int:todo_id>',view=views.todo_detail_view),
    path('cbv/',view=views.TodosListAPIView.as_view()),
    path('cbv/<int:todo_id>',view=views.TodoDetailAPIView.as_view()),
    
]
