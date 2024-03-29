# Generated by Django 5.0.3 on 2024-03-15 20:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('books', '0006_alter_book_created_at_alter_book_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.author'),
        ),
    ]
