# Generated by Django 3.1.4 on 2021-01-03 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('props_app', '0002_auto_20201217_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='wishlist',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]