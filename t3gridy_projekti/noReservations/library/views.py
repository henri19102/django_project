from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from .models import Book, Reservation, Author
from users.models import Profile
from django.urls import reverse
from django.contrib import messages
from .forms import ReviewForm
import random


def libraryIndex(request):
    max_id = Book.objects.order_by('-id')[0].id
    random_id = random.randint(1, max_id + 1)
    book = Book.objects.filter(id__gte=random_id)[0]
    context = { 'book' : book}
    return render(request, 'library/index.html',context)

@login_required     
def returnSuccess(request, book_id):
    Reservation.objects.filter(book_id = book_id).delete()
    messages.success(request, f'Book has been returned succesfully')
    return redirect('profile')

@login_required     
def success(request, book_id):
    book = get_object_or_404(Book, pk=book_id) # Haetaan kirja
    reserv = Reservation(book = book, loaner = request.user.profile) # Luodaan tietokantaan merkintä
    reserv.save()
    messages.success(request, f'{book.book_name} has been loaned Succesfully')
    return redirect('booking')

@login_required 
def loan(request, book_id):
    Book.objects.filter(pk = book_id).update(loaned=True) # Haetaan kirja
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a user hits the Back button.
    return HttpResponseRedirect(reverse('success', args=(book_id,))) # Ohjataan success funktioon

@login_required 
def returnBook(request, book_id):
    Book.objects.filter(pk = book_id).update(loaned=False) 
    return HttpResponseRedirect(reverse('returnSuccess', args=(book_id,)))



class BookListView(ListView):
    model = Book 
    template_name= 'library/booking.html'
    context_object_name = 'books' #Tällä avaimella contenttiin käsiksi

    # muuten list view vaihtaa objecti avaimen Context_object_nameksi
    queryset = Book.objects.all()
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(author__author_name__icontains=query) | self.model.objects.filter(book_name__icontains=query)
        else:
            object_list = self.model.objects.all().order_by("book_name","loaned")
        return object_list
    paginate_by = 6

class BookDetailView(DetailView):
    model = Book
    








