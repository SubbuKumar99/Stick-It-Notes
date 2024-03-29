# Generated by Django 2.1.1 on 2019-07-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_poststorage_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poststorage',
            name='author',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='poststorage',
            name='colour',
            field=models.CharField(choices=[(1, 'Yellow'), (2, 'Green'), (3, 'Purple'), (4, 'Blue'), (5, 'Orange')], default='Yellow', max_length=6),
        ),
        migrations.AlterField(
            model_name='poststorage',
            name='content',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='poststorage',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
