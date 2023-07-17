from django.contrib import admin
from .models import Book, BookReview, Author

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'avg_rating',
        'image',
        'has_options'
    )

    ordering = ('name',)


admin.site.register(Book, BookAdmin)
admin.site.register(BookReview)
admin.site.register(Author)
