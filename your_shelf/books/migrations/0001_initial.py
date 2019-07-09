# Generated by Django 2.1.7 on 2019-07-09 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/books/', verbose_name='画像')),
                ('deadline', models.DateField(verbose_name='返却日')),
                ('author', models.CharField(blank=True, max_length=255, null=True, verbose_name='著者')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='価格')),
                ('abstract', models.TextField(blank=True, null=True, verbose_name='要約')),
                ('publisher', models.CharField(blank=True, max_length=255, null=True, verbose_name='出版社')),
                ('publish_date', models.DateField(blank=True, null=True, verbose_name='出版日')),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='名前')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/users/', verbose_name='フォト')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Eメールアドレス')),
                ('password', models.CharField(max_length=128, verbose_name='パスワード')),
                ('books', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='本')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
