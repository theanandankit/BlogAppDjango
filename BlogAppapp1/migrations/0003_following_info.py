# Generated by Django 3.0.8 on 2020-07-30 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogAppapp1', '0002_auto_20200730_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Following_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_list1', to=settings.AUTH_USER_MODEL)),
                ('whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_list2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
