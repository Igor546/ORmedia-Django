from django.db import models


# python manage.py makemigrations
# python manage.py migrate

# Категория товара
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    # Чтобы в админке имя категории было не "Category object (1)" , а "self.name" (Смартфоны)
    def __str__(self):
        return self.name


# Бренд товара
class Brand(models.Model):
    name = models.CharField(max_length=100)

    # Чтобы в админке имя категории было не "Category object (1)" , а "self.name" (Смартфоны)
    def __str__(self):
        return self.name


# Сохранения изображений (работа с именами)
def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)  # Имя папки / Имя файла


# Товар
class Product(models.Model):
    # ForeignKey. Внешний-ключ (у одного товара может быть только одна категория/бренд)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)  # (Всего цифр <=9, после запятой 2)
    available = models.BooleanField(default=True)  # Товар Активен/Неактивен

    def __str__(self):
        return self.title
