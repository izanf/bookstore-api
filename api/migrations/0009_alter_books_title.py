# Generated by Django 4.0.4 on 2022-05-24 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_books_is_bn_alter_books_is_bn_13'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
