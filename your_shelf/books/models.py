from django.db import models

# Create your models here.

class Book(models.Model):
    """本モデル"""
    class Meta:
        # テーブル名を定義
        db_table = 'book'
        app_label='books'

    # フィールドを定義
    title = models.CharField(verbose_name='タイトル', max_length=255)
    image = models.ImageField(verbose_name='画像', null=True, blank=True, upload_to='images/books/')
    deadline = models.DateField(verbose_name='返却日')
    author = models.CharField(verbose_name='著者', max_length=255, null=True, blank=True)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    abstract = models.TextField(verbose_name='要約', null=True, blank=True)
    publisher = models.CharField(verbose_name='出版社', max_length=255, null=True, blank=True)
    publish_date = models.DateField(verbose_name='出版日', null=True, blank=True)

    def __str__(self):
        # 管理画面などで表示するstrにtitleを設定
        return self.title
