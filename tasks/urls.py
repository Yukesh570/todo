from django.urls import path
from . import views
urlpatterns=[
    path('',views.index, name="list" ),
    path('update_task', views.updateTask, name="update_task"),
    # path('delete_task/<str:pk>', views.deleteTask, name="delete_task"),
    path('search', views.search, name="search"),

]