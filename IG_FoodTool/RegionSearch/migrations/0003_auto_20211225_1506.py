# Generated by Django 3.2.9 on 2021-12-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegionSearch', '0002_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='total',
            name='Content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='total',
            name='PictureUrl',
            field=models.URLField(blank=True),
        ),
    ]
