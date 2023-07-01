from django.contrib import admin
from .models import Book, BookReview

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'price',
        'avg_rating',
        'image',
    )

    ordering = ('name',)


admin.site.register(Book, BookAdmin)
admin.site.register(BookReview)
