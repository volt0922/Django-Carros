# Generated by Django 3.2.10 on 2022-03-07 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0016_auto_20220301_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='fotosCarro',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='carro',
            name='garantia',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]