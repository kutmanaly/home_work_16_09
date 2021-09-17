from django.db import models

from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product, Category

User = get_user_model()

RATING_CHOICES = (
    (1, 'Плохо'),
    (2, 'Ну, так себе'),
    (3, 'Неплохо'),
    (4, 'Хорошо'),
    (5, 'Отлично')
)


class Review(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name='Товар')
    text = models.TextField('Текст')
    rating = models.IntegerField(choices=RATING_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat', verbose_name='категория')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def str(self):
        return f'Продукт: {self.product}, Автор: {self.author}, Оценка: {self.rating}'
