# Generated by Django 4.2.3 on 2023-07-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture_app', '0002_customer_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
            ],
        ),
    ]
