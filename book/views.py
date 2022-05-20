from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect,reverse
from . import models, forms


def all_books(request):
    queryset = models.Book.objects.all()
    return render(request, "books.html", {"books": queryset})


def get_book_detail(request, id):
    object = get_object_or_404(models.Book, id=id)
    return render(request, "book_detail.html", {"book": object})


def add_books(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse("Books Created successfully")
            return redirect(reverse("books_url:books_all_url"))
    else:
        form = forms.BookForm()
    return render(request, "add_books.html", {"form": form})
