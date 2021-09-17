from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, primary_key=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField('название', max_length=250)
    description = models.TextField('описание')
    price = models.IntegerField('цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_', verbose_name='категория')

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'




