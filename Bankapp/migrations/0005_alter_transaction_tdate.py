# Generated by Django 3.2.1 on 2021-07-05 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bankapp', '0004_auto_20210705_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='tdate',
            field=models.DateField(),
        ),
    ]
