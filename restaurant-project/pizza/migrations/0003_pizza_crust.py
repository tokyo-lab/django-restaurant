# Generated by Django 4.1.7 on 2023-03-18 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_crust_remove_pizza_crust'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='crust',
            field=models.CharField(default='Regular', max_length=100),
        ),
    ]
