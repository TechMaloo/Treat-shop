# Generated by Django 5.0.1 on 2024-01-30 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_photofeed_textfeed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
    ]
