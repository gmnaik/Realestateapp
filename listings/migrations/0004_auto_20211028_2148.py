# Generated by Django 3.2.4 on 2021-10-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20211028_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(),
        ),
    ]