# Generated by Django 3.2.9 on 2021-12-25 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegionSearch', '0008_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='PostID',
        ),
    ]
