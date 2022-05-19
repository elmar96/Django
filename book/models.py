from django.db import models


class Book(models.Model):
    GENRE_CHOICE = (
        ("Drama", "Drama"),
        ("Fantasy", "Fantasy"),
        ("Thriller", "Thriller"),
        ("Romance", "Romance"),
        ("Westerns", "Westerns"),
        ("Literary Fiction", "Literary Fiction"),
        ("Humor", "Humor"),
        ("Motivational", "Motivational"),
        ("Historical Fiction", "Historical Fiction")


    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="")
    author = models.CharField(max_length=30)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE)
    year_of_issue = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    age_control = models.PositiveIntegerField()

    def __str__(self):
        return self.title
