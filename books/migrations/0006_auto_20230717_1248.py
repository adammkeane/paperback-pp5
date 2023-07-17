# Generated by Django 3.2.19 on 2023-07-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_rename_has_formats_book_has_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('bio', models.TextField(blank=True, max_length=10000)),
                ('books', models.ManyToManyField(to='books.Book')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
