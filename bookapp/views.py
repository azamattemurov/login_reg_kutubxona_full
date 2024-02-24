from django.forms import ImageField
from django.http import request
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Book
from .bookform import BookForm
from django.urls import reverse_lazy


class BookListView(ListView):
    model = Book
    template_name = 'book-list.html'
    context_object_name = 'books'
    ordering = ['title']


class BookDetailView(DetailView):
    model = Book
    template_name = 'book-detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    class_form = BookForm
    fields = ['title', 'description', 'author', 'price']
    template_name = 'book-create.html'
    success_url = reverse_lazy('book-list')


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'description', 'author', 'price']
    template_name = 'book-update.html'
    class_form = BookForm
    success_url = reverse_lazy('book-list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book-delete.html'
    success_url = reverse_lazy('book-list')
