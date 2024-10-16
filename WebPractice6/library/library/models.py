from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=100)
    date_of_publication = models.DateField()
    page_count = models.IntegerField()
    total_rating = models.FloatField()

    def __str__(self):
        return self.book_title


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name


class BookGenres(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta: 
        unique_together = ('book', 'genre')


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.order_id} by {self.user.first_name} {self.user.last_name}"
