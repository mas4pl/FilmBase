# Generated by Django 2.2.6 on 2020-05-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addfilms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.SmallIntegerField(),
        ),
    ]