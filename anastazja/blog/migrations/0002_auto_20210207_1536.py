# Generated by Django 2.2.17 on 2021-02-07 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='media/blog/', verbose_name='Изображение'),
        ),
    ]