# Generated by Django 4.0.8 on 2022-12-22 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deezer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='artist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
