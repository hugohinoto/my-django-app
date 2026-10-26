from django.contrib import admin
from django.urls import path
from . import views  # ← さっき作ったviewsを読み込む

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # ← トップページ（URLの末尾が空）の行き先を設定！
]
