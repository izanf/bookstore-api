from django.urls import path
from . import views

urlpatterns = [
  path('api/v1/books', views.BooksList.as_view()),
  path('api/v1/books/<int:pk>/', views.BookItem.as_view()),
]