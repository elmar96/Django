from django.urls import path
from . import views

app_name = "books_url"
urlpatterns = [
    path('books/', views.all_books, name="books_all_url"),
    path('books/<int:id>/', views.get_book_detail, name="books_url"),
    path('add-books/', views.add_books, name="add_books"),
]