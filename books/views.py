from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Avg
from django.views import generic, View
from django.db.models.functions import Lower

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
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                books = books.annotate(lower_name=Lower('name'))
            if sortkey == 'rating':
                sortkey = 'avg_rating_sort'
                books = books.annotate(
                    avg_rating_sort=Avg('book_review__rating'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            books = books.order_by(sortkey) 

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('books'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query) | Q(author__icontains=query)
            books = books.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'books': books,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'books/books.html', context)


def book_detail(request, book_id):
    """ View to show details of one book """
    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book,
    }

    return render(request, 'books/book_detail.html', context)
