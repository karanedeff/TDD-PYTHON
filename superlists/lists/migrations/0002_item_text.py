# Generated by Django 4.1.7 on 2023-02-20 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default='-', verbose_name='-'),
            preserve_default=False,
        ),
    ]
