# Generated by Django 3.0.8 on 2020-08-09 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='Hello There', max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=150, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_details', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.CharField(max_length=10, unique=True)),
                ('group_description', models.CharField(max_length=100)),
                ('url', models.CharField(default='NA', max_length=200)),
                ('group_code', models.CharField(max_length=6)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='BlogAppapp1.Groups', to_field='group_id')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Following_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_list1', to=settings.AUTH_USER_MODEL)),
                ('whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_list2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=2000)),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(max_length=20)),
                ('status', models.CharField(default='public', max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_name', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='BlogAppapp1.Groups', to_field='group_id')),
            ],
        ),
    ]
