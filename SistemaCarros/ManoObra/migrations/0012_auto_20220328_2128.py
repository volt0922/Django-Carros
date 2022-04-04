# Generated by Django 3.2.10 on 2022-03-28 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Presupuestos', '0009_auto_20220328_2128'),
        ('ManoObra', '0011_auto_20220301_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manoobra',
            name='descuento',
        ),
        migrations.RemoveField(
            model_name='manoobra',
            name='numeroDescuento',
        ),
        migrations.RemoveField(
            model_name='manoobra',
            name='total',
        ),
        migrations.AddField(
            model_name='manoobra',
            name='estimate_ids',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Presupuestos.presupuestos'),
        ),
    ]
