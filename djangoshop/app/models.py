from django.db import models


# python manage.py makemigrations
# python manage.py migrate

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    # Чтобы в админке имя категории было не "Category object (1)" , а "self.name" (Смартфоны)
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    # Чтобы в админке имя категории было не "Category object (1)" , а "self.name" (Смартфоны)
    def __str__(self):
        return self.name
