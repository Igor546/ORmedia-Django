from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse
from transliterate import translit


# ВСЕГДА ПРИ ИЗМЕНЕНИИ/СОЗДАНИИ МОДЕЛИ после ПРОПИСЫВАЕМ ЭТО:
# python manage.py makemigrations
# python manage.py migrate

# Категория товара
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)  # blank=True - убрать необходимость заполнения формы

    # Чтобы в админке имя категории было не "Category object (1)" , а "self.name" (Смартфоны)
    def __str__(self):
        return self.name

    # Возврат url для категорий (используем в base.html)
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})


# Преобразует "name" в "slug"
def pre_save_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        # Преобразуем кирилицу в транслит, а транслит в slag-формат
        slug = slugify(translit(str(instance.name), reversed=True))
        instance.slug = slug


pre_save.connect(pre_save_category_slug, sender=Category)


# Бренд товара
class Brand(models.Model):
    name = models.CharField(max_length=100)

    # Чтобы в админке имя бренда было не "Brand object (1)" , а "self.name"
    def __str__(self):
        return self.name


# Сохранения изображений (работа с именами)
def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)  # Имя папки / Имя файла


# Переопределение метода all для Product.objects (который используем в views)
class ProductManager(models.Manager):
    # Возвращает список продуктов имеющих атрибут available=True
    def all(self, *args, **kwards):
        return super(ProductManager, self).get_queryset().filter(available=True)

    # Возвращает список продуктов имеющих категорию ноутбук
    def notebooks(self, *args, **kwards):
        return super(ProductManager, self).get_queryset().filter(category=Category.objects.all()[1])


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
    objects = ProductManager()

    def __str__(self):
        return self.title

    # Возврат url для продуктов (используем в base.html)
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})


# Промежуточный продукт (для корзины)
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Продукт
    count = models.PositiveIntegerField(default=1)  # Количество
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)  # Для изменения количества

    def __str__(self):
        return "Cart item for product {}".format(self.product.title)


# Модель корзины
class Cart(models.Model):
    # Можем в корзину добавить множество CartItem (связь Многие ко многим)
    items = models.ManyToManyField(CartItem, blank=True)  # blank=True - убрать необходимость заполнения формы
    all_price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)

    def add_to_cart(self, product_slug):
        cart = self
        product = Product.objects.get(slug=product_slug)
        new_item, _ = CartItem.objects.get_or_create(product=product, price=product.price)
        if new_item not in cart.items.all():
            cart.items.add(new_item)
            cart.save()

    def del_to_cart(self, product_slug):
        cart = self
        product = Product.objects.get(slug=product_slug)
        for cart_item in cart.items.all():
            if cart_item.product == product:
                cart.items.remove(cart_item)
                cart.save()
