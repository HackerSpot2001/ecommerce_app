# Generated by Django 4.1.5 on 2023-04-29 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('IN', 'Indian Rupee'), ('USD', 'US Dollar')], max_length=20, null=True),
        ),
    ]
