from django.urls import path,include
from . import views
from .views import BookListView, BookDetailView


urlpatterns = [
    path('', views.libraryIndex, name='library-index'),
    path('booking/', BookListView.as_view(), name='booking'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('<int:book_id>/loan/', views.loan,name='loan'),
    path('<int:book_id>/success/', views.success, name='success'),
    
]
