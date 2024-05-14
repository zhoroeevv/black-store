from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_products',
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    description = models.TextField(
        verbose_name = "Описание"
    )
    price = models.PositiveBigIntegerField(
        verbose_name = "Цена"
    )
    image = models.ImageField(
        upload_to = "product_images/",
        verbose_name = "Фотография"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"