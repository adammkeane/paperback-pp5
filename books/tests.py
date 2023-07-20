from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Book, BookReview
from django.shortcuts import get_object_or_404


class TestBooksViewsAndModels(TestCase):
    """
    Test cases for books app as logged in user
    """

    def setUp(self):
        """ Setup test """
        username = 'adammmmadaaAA'
        password = '*456MoleManeeer'
        user_model = get_user_model()
        # Create user
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

        # Create book
        Book.objects.create(
            name='Test title',
            description='test description',
            price='3',
        )

        # Create Reviews for Book
        BookReview.objects.create(
            title='Test review 1',
            book=get_object_or_404(Book.objects, name='Test title'),
            username=self.user,
            rating=2.5
        )

        BookReview.objects.create(
            title='Test review 2',
            book=get_object_or_404(Book.objects, name='Test title'),
            username=self.user,
            rating=5
        )

        BookReview.objects.create(
            title='Test review 3',
            book=get_object_or_404(Book.objects, name='Test title'),
            username=self.user,
            rating=4
        )

    def test_book_string_method_returns_name(self):
        """ Test Book Model string method """
        book = get_object_or_404(Book.objects, name='Test title')
        self.assertEqual(str(book), 'Test title')

    def test_book_avg_rating_method(self):
        """ Test Book Model avg_rating method """
        book = get_object_or_404(Book.objects, name='Test title')
        self.assertEqual(str(book.avg_rating()), '3.8')

    def test_book_reviews_total_method(self):
        """ Test Book Model reviews_total method """
        book = get_object_or_404(Book.objects, name='Test title')
        self.assertEqual(book.reviews_total(), 3)

    def test_book_review_string_method_returns_name(self):
        """ Test BookReview Model string method """
        review = get_object_or_404(BookReview.objects, title='Test review 1')
        self.assertEqual(str(review), 'Test review 1')

    def test_books_page(self):
        """ Test all books page """
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/books.html')

    def test_book_detail(self):
        """ Test book Detail """
        book = get_object_or_404(Book.objects, name='Test title')
        response = self.client.get(f'/books/{book.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_detail.html')

    def test_book_create(self):
        """ Test Book Create """
        response = self.client.get('/books/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/add_book.html')

    def test_book_edit(self):
        """ Test book Edit """
        book = get_object_or_404(Book.objects, name='Test title')
        response = self.client.get(f'/books/edit/{book.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/edit_book.html')

    def test_profile_page(self):
        """ Test Profile Page """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_review_create(self):
        """ Test Review Create """
        book = get_object_or_404(Book.objects, name='Test title')
        response = self.client.get(f'/books/book_review_create/{book.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_review_create.html')


class TestBooksViewsLoggedOut(TestCase):
    """
    Test cases for books app as logged out user
    """

    def setUp(self):
        """ Setup test """
        username = 'adammmmadaaAA'
        password = '*456MoleManeeer'
        user_model = get_user_model()
        # Create user
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True
        )

        # Create book
        Book.objects.create(
            name='Test title',
            description='test description',
            price='3',
        )

    def test_book_create(self):
        """ Test book Create """
        response = self.client.get('/books/add/')
        self.assertEqual(response.status_code, 302)

    def test_book_edit(self):
        """ Test book Edit """
        book = get_object_or_404(Book.objects, name='Test title')
        response = self.client.get(f'/books/edit/{book.id}/')
        self.assertEqual(response.status_code, 302)

    def test_book_delete(self):
        """ Test book Delete """
        book = get_object_or_404(Book.objects, name='Test title')
        response = self.client.get(f'/books/delete/{book.id}/')
        self.assertEqual(response.status_code, 302)

    def test_review_create(self):
        """ Test Review Create """
        book = get_object_or_404(Book.objects, name='Test title')
        response = self.client.get(f'/books/book_review_create/{book.pk}/')
        self.assertEqual(response.status_code, 302)
