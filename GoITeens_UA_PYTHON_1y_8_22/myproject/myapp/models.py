from django.db import models
from django.contrib.auth.models import User


class Dish(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/')

    def __str__(self):
        return f'Name: {self.name}, Description: {self.desc}, Price: {self.price}'


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating_choices = (
        ('terrible', 'Terrible'),
        ('bad', 'Bad'),
        ('average', 'Average'),
        ('good', 'Good'),
        ('excellent', 'Excellent'),
    )
    rating = models.CharField(max_length=10, choices=rating_choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.author.username} ({self.rating})'


class UserProfile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Table(models.Model):
    name = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.name)


class TableReservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    table_number = models.ForeignKey(Table, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - Table {self.table_number}'
