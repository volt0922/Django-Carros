# Generated by Django 3.2.10 on 2022-05-09 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('fax', models.CharField(blank=True, max_length=255)),
                ('celular', models.CharField(max_length=255)),
                ('posicion', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=255)),
                ('vehiculos_poseidos', models.ManyToManyField(blank=True, to='carros.Carro')),
            ],
        ),
    ]
