# Generated by Django 3.2.4 on 2023-09-20 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20230919_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno_has_genero',
            name='id',
        ),
        migrations.AddField(
            model_name='alumno_has_genero',
            name='idalumno_has_genero',
            field=models.AutoField(db_column='idalumno_has_genero', default=1, primary_key=True, serialize=False),
        ),
    ]
