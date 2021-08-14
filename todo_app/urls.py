from django.contrib import admin
from django.urls import path
from todo_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('addtodo', views.add_todo, name='addtodo'),
    path('logout', views.signout, name='signout'),
    path('delete-todo/<int:id>', views.delete_todo, name='delete-todo'),
    path('change-status/<int:id>/<str:status>', views.change_status, name='change-status'),
]
