# Generated by Django 3.2.10 on 2022-05-09 08:48

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')),
                ('location', models.CharField(default=0, max_length=100)),
                ('phone1', models.IntegerField(default=0)),
                ('phone2', models.IntegerField(default=0)),
                ('fax', models.IntegerField(default=0)),
                ('email', models.CharField(default=0, max_length=100)),
                ('website', models.CharField(default=0, max_length=100)),
                ('socialMedia1', models.CharField(default=0, max_length=100)),
                ('socialMedia2', models.CharField(default=0, max_length=100)),
                ('socialMedia3', models.CharField(default=0, max_length=100)),
                ('alternativeContact', models.CharField(default=0, max_length=100)),
                ('country', models.CharField(choices=[('EUA', 'EUA'), ('Canada', 'Canada'), ('Other', 'Other')], default=0, max_length=100)),
                ('address', models.CharField(default=0, max_length=100)),
                ('city', models.CharField(default=0, max_length=100)),
                ('state', models.CharField(default=0, max_length=100)),
                ('zip', models.CharField(default=0, max_length=10)),
                ('user', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
