# Generated by Django 4.1.2 on 2022-11-16 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tur', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='photo',
            field=models.ImageField(upload_to='img/city/'),
        ),
    ]