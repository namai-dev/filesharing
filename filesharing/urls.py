from django.urls import path
from .views import Hello, FileManager

urlpatterns = [
    path("",FileManager.as_view() ),
    path("file/<int:pk>/", FileManager.as_view())
   # path("/upload/", FileManager.as_view())
]
