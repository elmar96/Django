from django.urls import path
from . import views

app_name = "books_url"
urlpatterns = [
    path('books/', views.all_books, name="books_all_url"),
    path('books/latest/', views.all_books_latest, name="latest"),
    path('books/drama/', views.all_books_drama, name="drama"),
    path('books/fantasy/', views.all_books_fantasy, name="frama"),
    path('books/thriller/', views.all_books_thriller, name="thriller"),
    path('books/romance/', views.all_books_romance, name="Romance"),
    path('books/westerns/', views.all_books_westerns, name="westerns"),
    path('books/literary_fiction/', views.all_books_literary_fiction, name="Literary Fiction"),
    path('books/humor/', views.all_books_humor, name="Humor"),
    path('books/motivational/', views.all_books_motivational, name="Motivational"),
    path('books/historical_fiction/', views.all_books_historical_fiction, name="Historical Fiction"),
    path('books/masnavyi/', views.all_books_masnavyi, name="fantasy"),









    path('books/<int:id>/', views.get_book_detail, name="books_url"),
    path('books/<int:id>/update/', views.book_update, name="books_update"),
    path('books/<int:id>/delete/', views.book_delete, name="books_delete"),
    path('add-books/', views.add_books, name="add_books"),
]