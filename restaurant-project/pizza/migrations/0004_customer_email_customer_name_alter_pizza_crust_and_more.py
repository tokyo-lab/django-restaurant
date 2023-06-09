# Generated by Django 4.1.7 on 2023-03-19 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_pizza_crust'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='pizza',
            name='crust',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.crust'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.size')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.crust')),
            ],
        ),
    ]
