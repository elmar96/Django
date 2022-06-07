from django.contrib import admin
from . import models


class CarsAdmin(admin.ModelAdmin):
    model = models.Cars
    list_display = [
        "id",
        "link",
        "title",
    ]

    list_filter = [
        "title",
    ]
    # list_editable = ["title", ]
    search_fields = [
        "tile",
    ]


class AgroAdmin(admin.ModelAdmin):
    model = models.Agro
    list_display = [
        "id",
        "link",
        "title",
    ]
    # сортировка
    list_filter = [
        "title",
    ]

    # редактирования
    list_editable = [
        "title",
    ]

    # поиск
    search_fields = [
        "tile",
    ]


admin.site.register(models.Cars, CarsAdmin)
admin.site.register(models.Agro, AgroAdmin)
admin.site.register(models.Eda)
