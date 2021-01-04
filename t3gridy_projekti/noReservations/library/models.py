from django.db import models
import datetime
from datetime import date, timedelta
from django.contrib import admin

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.author_name}'

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)
    description = models.TextField()
    pub_date = models.DateField()
    #was_published_recently.admin_order_field = 'pub_date'
    image = models.ImageField(default = 'default.jpg', upload_to = 'book_pics')
    loaned = models.BooleanField(default=False)

    def __str__(self):
        return f'Book name: {self.book_name}'


    

class Reservation(models.Model):
    def get_expdate():
        return date.today()+timedelta(days=14)

    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    loaner = models.ForeignKey("users.Profile", on_delete=models.CASCADE)
    expirydate = models.DateField(default=get_expdate)

    class Meta:
        ordering=['-loaner']

    def __str__(self):
        return f'{self.loaner}, {self.book}, Exp: {self.expirydate.strftime("%d.%m.%Y")}'

    

