from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="商品名")
    price = models.IntegerField(verbose_name="価格（円）")
    description = models.TextField(verbose_name="商品説明", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="登録日時")

    def __str__(self):
        return self.name
