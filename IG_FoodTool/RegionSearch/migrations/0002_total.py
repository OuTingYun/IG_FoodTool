# Generated by Django 3.2.9 on 2021-12-25 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegionSearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='total',
            fields=[
                ('PostID', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('AccountName', models.CharField(max_length=32)),
                ('PlaceID', models.PositiveIntegerField()),
            ],
        ),
    ]
