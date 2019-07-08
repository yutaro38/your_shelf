from django.db import models
from books.models import Book

# Create your models here.
class User(models.Model):
    """ユーザモデル"""
    class Meta:
        # テーブル名を定義
        db_table = 'user'
        app_label= 'books'

    # フィールドを定義
    name = models.CharField(verbose_name='名前', max_length=255, unique=True)
    photo = models.ImageField(verbose_name='フォト', blank=True, null=True, upload_to='images/users/')
    books = models.ForeignKey(Book, verbose_name='本', null=True, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='Eメールアドレス', blank=True)
    password = models.CharField(verbose_name='パスワード', max_length=128)
    def __str__(self):
        # 管理画面などで表示するstrにtitleを設定
        return self.name
