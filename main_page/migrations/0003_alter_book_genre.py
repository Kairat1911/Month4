# Generated by Django 5.1.2 on 2024-11-25 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_alter_book_created_at_alter_book_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='main_page.genre'),
        ),
    ]
