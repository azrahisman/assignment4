from django.urls import path
from todolist.views import show_todolist, create_task, register, login_user, logout_user, show_json, todolist_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_task, name='create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show_json'),
    path('ajax/', todolist_ajax, name='todolist_ajax'),
]