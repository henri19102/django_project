# Generated by Django 3.1.1 on 2020-09-28 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20200928_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authors',
            new_name='author',
        ),
    ]
