# Generated by Django 2.0.5 on 2019-05-11 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
        ('authorization', '0002_auto_20190507_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='focus_app',
            field=models.ManyToManyField(to='apis.App'),
        ),
    ]