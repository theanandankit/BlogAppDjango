# Generated by Django 3.0.8 on 2020-08-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAppapp1', '0006_auto_20200804_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='url',
            field=models.CharField(default='NA', max_length=200),
        ),
    ]