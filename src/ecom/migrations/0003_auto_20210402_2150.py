# Generated by Django 3.1.7 on 2021-04-02 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='static/images/placeholder.png', null=True, upload_to=''),
        ),
    ]