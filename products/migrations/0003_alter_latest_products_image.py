# Generated by Django 4.2.7 on 2023-11-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_latest_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latest_products',
            name='image',
            field=models.ImageField(upload_to='static/images/latest-products/'),
        ),
    ]
