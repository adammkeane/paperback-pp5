from django.views.generic import ListView
from books.models import Book


class HomePage(ListView):
    """View to show the home page, including the latest 3 books"""
    template_name = 'home/index.html'
    queryset = Book.objects.all()[:3]
    context_object_name = "books"
