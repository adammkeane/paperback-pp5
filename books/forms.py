from django import forms
from .widgets import CustomClearableFileInput
from .models import Book, BookReview


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)


class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = (
            'title',
            'description',
            'rating',
        )
