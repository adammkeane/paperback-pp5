from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.views import generic, View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models.functions import Lower

from .models import Book, Author
from .forms import BookForm, BookReviewForm


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
                description__icontains=query) | Q(
                    author__name__icontains=query)
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
    authors = book.author_set.all()
    reviews = book.book_review.order_by('-created_on')
    if len(reviews) > 0:
        no_reviews = False
    else:
        no_reviews = True

    context = {
        'book': book,
        'reviews': reviews,
        'no_reviews': no_reviews,
        'authors': authors,
    }

    return render(request, 'books/book_detail.html', context)


@login_required
def add_book(request):
    """ Add a book to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Successfully added book!')
            return redirect(reverse('book_detail', args=[book.id]))
        else:
            messages.error(
                request,
                'Failed to add book. Please ensure the form is valid.'
            )
    else:
        form = BookForm()

    template = 'books/add_book.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_book(request, book_id):
    """ Edit a book in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated book!')
            return redirect(reverse('book_detail', args=[book.id]))
        else:
            messages.error(
                request,
                'Failed to update book. Please ensure the form is valid.')
    else:
        form = BookForm(instance=book)
        messages.info(request, f'You are editing {book.name}')

    template = 'books/edit_book.html'
    context = {
        'form': form,
        'book': book,
    }

    return render(request, template, context)


@login_required
def delete_book(request, book_id):
    """ Delete a book from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    messages.success(request, 'Book deleted!')
    return redirect(reverse('books'))


class BookReviewCreate(UserPassesTestMixin, View):
    """View to handle book review creation"""

    def get(self, request, book_id, *args, **kwargs):
        return render(
            request,
            'books/book_review_create.html',
            {
                'book_form': BookReviewForm(),
                'book_id': book_id
            },
        )

    def post(self, request, book_id, *args, **kwargs):
        book_form = BookReviewForm(request.POST)

        if book_form.is_valid():
            """If review form is valid, add review to database"""
            entry = book_form.save(commit=False)
            entry.username = request.user
            book = get_object_or_404(Book.objects, id=book_id)
            entry.book = book
            entry.save()

            messages.success(request, 'Review Added!')
            return redirect(reverse('book_detail', args=[book.id]))
        else:
            """If review form is not valid, return to form page"""
            return render(
                request,
                'books/book_review_create.html',
                {
                    'book_form': BookReviewForm(data=request.POST),
                },
            )

    def test_func(self):
        """Mixin Test"""
        return self.request.user.is_authenticated


def author(request, author_id):
    """ View to show author page """
    author = get_object_or_404(Author, pk=author_id)
    books = author.books.all()

    context = {
        'author': author,
        'books': books,
    }

    return render(request, 'books/author.html', context)
