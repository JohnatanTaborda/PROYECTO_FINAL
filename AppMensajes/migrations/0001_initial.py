# Generated by Django 4.1.3 on 2022-12-01 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Rol', models.CharField(max_length=50)),
                ('Identificacion', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asunto', models.CharField(max_length=200)),
                ('Cuerpo', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Identificacion', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vacante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_Vacante', models.CharField(max_length=80)),
                ('Id_Vacante', models.IntegerField()),
            ],
        ),
    ]
