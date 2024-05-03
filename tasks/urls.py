from django.urls import path
from . import views
urlpatterns=[
    path('',views.index, name="list" ),
    # path('delete_task/<str:pk>', views.deleteTask, name="delete_task"),
    path('search', views.search, name="search"),
    path('error', views.error,name="error"),
    path('updatetask', views.updateTask,name="update_task"),

]