from todoapp import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

urlpatterns = [
    path('todoapp/', views.todo_list.as_view()),
    path('todoapp/<int:pk>/', views.todo_detail.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)