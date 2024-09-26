# Generated by Django 5.1.1 on 2024-09-14 23:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=15)),
                ('domicilio', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_solicitud', models.DateField(auto_now_add=True)),
                ('fecha_entrega', models.DateTimeField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('EN_PROCESO', 'En proceso'), ('COMPLETADO', 'Completado')], default='PENDIENTE', max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.cliente')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.servicio')),
            ],
        ),
    ]
