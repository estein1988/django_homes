# Generated by Django 3.1.2 on 2020-10-28 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('social_level', models.JSONField(default=dict)),
            ],
        ),
        migrations.AlterField(
            model_name='home',
            name='lat_long',
            field=models.JSONField(default=dict),
        ),
    ]
