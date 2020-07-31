# Generated by Django 3.0.8 on 2020-07-31 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogAppapp1', '0004_blog_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.CharField(max_length=10)),
                ('group_description', models.CharField(max_length=100)),
                ('group_code', models.CharField(max_length=6)),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
