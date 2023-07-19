# Generated by Django 4.2.3 on 2023-07-18 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture_app', '0003_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('condition', models.CharField(max_length=100)),
                ('days_to_deliver', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=500)),
                ('rate', models.FloatField()),
            ],
        ),
    ]
