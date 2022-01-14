# Generated by Django 3.2.9 on 2021-12-25 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegionSearch', '0007_alter_total_pictureurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('PostID', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('AccountName', models.CharField(max_length=32)),
                ('PlaceID', models.PositiveIntegerField()),
                ('Content', models.TextField(blank=True)),
                ('Place', models.CharField(max_length=32, null=True)),
                ('PictureUrl', models.CharField(max_length=5000, null=True)),
            ],
        ),
    ]
