# Generated by Django 2.2.3 on 2019-08-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_cart_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='app.CartItem'),
        ),
    ]
