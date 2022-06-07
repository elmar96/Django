from django.db import models


class Cars(models.Model):
    class Meta:
        verbose_name = "Автомабиль"
        verbose_name_plural = "Автомабили"

    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")


class Agro(models.Model):
    class Meta:
        verbose_name = "Агро"
        verbose_name_plural = "Агро"

    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")


class Eda(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")
