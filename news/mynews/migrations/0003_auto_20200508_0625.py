# Generated by Django 3.0 on 2020-05-08 06:25

from django.db import migrations, models
import mynews.models


class Migration(migrations.Migration):

    dependencies = [
        ('mynews', '0002_auto_20200508_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image_there',
            field=models.ImageField(blank=True, upload_to=mynews.models.image_folder, verbose_name='Foto boshqalar N:3 700x600*'),
        ),
    ]