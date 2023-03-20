# Generated by Django 4.1.7 on 2023-03-20 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0006_alter_customer_email_alter_customer_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='addons',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pizza.addons'),
        ),
    ]
