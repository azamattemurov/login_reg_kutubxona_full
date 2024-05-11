from django.urls import path
from .views import *

app_name = 'books'
urlpatterns = [
    path('list/', BookListView.as_view(), name='list'),
    path('book-detail/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book-create/', BookCreateView.as_view(), name='book-create'),
    path('book-update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('book-delete/<int:pk>/', BookDeleteView.as_view(),name='book-delete'),
]
