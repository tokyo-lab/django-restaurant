# Generated by Django 4.1.7 on 2023-03-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0007_addons_pizza_addons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addons',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
