from django.db import models

# Create your models here.
class alumno(models.Model):
    idAlumno= models.IntegerField(primary_key=true,db_column='idAlumno')
    nameAlumno = models.CharField(max_length=100,db_column='nameAlumno')
    class Meta:
        db_table='Alumnos'