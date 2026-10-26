from django.shortcuts import render
from .models import Product  # ← 商品のデータ構造を読み込む

def home(request):
    products = Product.objects.all()  # ← データベースから全ての商品データを取ってくる！
    return render(request, 'index.html', {'products': products})  # ← HTMLに商品データを引き渡す！
