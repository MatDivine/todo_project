from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.TodosAllCURDWithViewSetsAPIView)


urlpatterns = [
    path('',view=views.all_todos),
    path('<int:todo_id>',view=views.todo_detail_view),
    path('cbv/',view=views.TodosListAPIView.as_view()),
    path('cbv/<int:todo_id>',view=views.TodoDetailAPIView.as_view()),
    path('mixins/',view=views.TodosListMixinAPIView.as_view()),  
    path('mixins/<int:pk>',view=views.TodosDetaileMixinAPIView.as_view()),  
    path('generics/',view=views.TodosListAndCreateGenericsAPIView.as_view()),  
    path('generics/<int:pk>',view=views.TodoRetrieveAndUpdateAndDestroyAPIView.as_view()),  
    path('viewsets/', include(router.urls)),
]
