# Generated by Django 2.1.1 on 2019-07-19 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190717_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='poststorage',
            name='colour',
            field=models.CharField(choices=[(1, 'Green'), (2, 'Yellow')], default='Yellow', max_length=6),
        ),
    ]
