from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Book


# class AllBooks(generic.TemplateView):
#     """View to show all books, including sorting and search queries"""
#     template_name = 'books/books.html'


# class AllBooks(generic.ListView):
#     """View to show all books, including sorting and search queries"""
#     model = Book
#     queryset = Book.objects.order_by('name')
#     template_name = 'books/books.html'
#     paginate_by = 10


def all_books(request):
    """ View to show all books, including sorting and search queries """
    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'books/books.html', context)


def book_detail(request, book_id):
    """ View to show details of one book """
    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'books/book_detail.html', context)
