from django.db import db_models as models  # Django 6.1スタイル
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="商品名")
    price = models.IntegerField(verbose_name="価格")
    description = models.TextField(verbose_name="商品説明")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
