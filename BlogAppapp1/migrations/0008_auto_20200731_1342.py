# Generated by Django 3.0.8 on 2020-07-31 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogAppapp1', '0007_auto_20200731_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmembers',
            name='member_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_info', to=settings.AUTH_USER_MODEL),
        ),
    ]