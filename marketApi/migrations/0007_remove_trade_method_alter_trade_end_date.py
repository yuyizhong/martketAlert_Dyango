# Generated by Django 4.1.7 on 2023-04-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketApi', '0006_alter_trade_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='method',
        ),
        migrations.AlterField(
            model_name='trade',
            name='end_date',
            field=models.DateField(),
        ),
    ]
