# Generated by Django 4.1.2 on 2022-11-01 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tur', '0002_alter_hotel_cityname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='cityName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='tur.city'),
        ),
        migrations.CreateModel(
            name='tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='img/tour/')),
                ('body', models.TextField(max_length=200)),
                ('event', models.BooleanField(default=False)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('hotelName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel', to='tur.hotel')),
            ],
        ),
    ]