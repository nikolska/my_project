# Generated by Django 2.2.17 on 2021-02-07 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='pictures', upload_to='media/services/', verbose_name='Изображение'),
        ),
    ]