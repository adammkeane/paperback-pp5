from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=10000)
    has_options = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def just_date_published_on(self):
        """Simplfies date"""
        return str(self.published_on)

    def avg_rating(self):
        """Calculates the mean average rating of a book"""
        reviews = self.book_review.all()
        if len(reviews) > 0:
            review_total = 0
            for review in reviews:
                review_total += review.rating
            avg_rating_raw = (review_total)/(len(reviews))
            avg_rating = round(avg_rating_raw, 1)
            return avg_rating
        else:
            return 'N/A'

    def reviews_total(self):
        """Counts number of reviews a book has"""
        reviews = self.book_review.all()
        return len(reviews)


RATING = (
    (0, "0"),
    (0.5, "0.5"),
    (1, "1"),
    (1.5, "1.5"),
    (2, "2"),
    (2.5, "2.5"),
    (3, "3"),
    (3.5, "3.5"),
    (4, "4"),
    (4.5, "4.5"),
    (5, "5")
)


class BookReview(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="book_review"
    )
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_rating"
    )
    title = models.CharField(max_length=50, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=10000, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(
        choices=RATING, max_digits=2, decimal_places=1
    )

    class Meta:
        # ordered in descending order, based on created_on value,
        # so that newest posts are first.
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def just_date_created_on(self):
        """Simplfies date"""
        return self.created_on.date()

    def just_date_updated_on(self):
        """Simplfies date"""
        return self.updated_on.date()


class Author(models.Model):
    name = models.CharField(max_length=100, null=True)
    books = models.ManyToManyField(Book)
    bio = models.TextField(max_length=10000, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
