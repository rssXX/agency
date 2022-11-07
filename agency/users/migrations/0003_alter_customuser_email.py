# Generated by Django 4.1.2 on 2022-11-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True, verbose_name='Электронная почта'),
        ),
    ]
