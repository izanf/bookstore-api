# Generated by Django 4.0.4 on 2022-05-24 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_books_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]