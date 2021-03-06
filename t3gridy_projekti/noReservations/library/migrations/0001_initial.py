# Generated by Django 3.1.1 on 2020-09-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('image', models.ImageField(default='default.jpg', upload_to='book_pics')),
            ],
        ),
    ]
