# Generated by Django 5.0.6 on 2024-06-14 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
