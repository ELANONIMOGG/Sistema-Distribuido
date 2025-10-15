from django.urls import path
from . import views

app_name = 'file_uploader'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload'),
    path('files/', views.list_files, name='list_files'),
    path('download/<str:filename>/', views.download_file, name='download'),
    path('delete/<str:filename>/', views.delete_file, name='delete'),
]