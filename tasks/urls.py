from django.urls import path
from . import views
urlpatterns=[
    path('',views.index, name="list" ),
    path('delete_item/<str:pk>', views.delete, name="delete_item"),
    path('search', views.search, name="search"),
    path('error', views.error,name="error"),
    path('updatetask', views.updateTask,name="update_task"),
    path('edit/<str:pk>', views.edit,name="edit"),
    path('table', views.table,name="table"),


]