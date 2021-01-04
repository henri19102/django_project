from django.contrib import admin
from .models import Book, Reservation, Author

class BookAdmin(admin.ModelAdmin):
    list_display=('book_name', 'loaned')

class ReservationAdmin(admin.ModelAdmin):
    ordering= ('loaner')

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Reservation)
# Register your models here.
