from django.db import models

# Create your models here.
class Genero(models.Model):
    idGenero = models.AutoField(primary_key=True,db_column='idGenero')
    tipoGenero = models.TextField(db_column='tipoGenero')
    class Meta:
        db_table='Generos'

class Alumnos(models.Model):
    idAlumno = models.IntegerField(primary_key=True,db_column='idAlumno')
    nameAlumno = models.CharField(max_length=100,db_column='nameAlumno')
    class Meta:
        db_table='Alumnos'
        
class alumno_has_genero(models.Model):
    idalumno_has_genero = models.AutoField(primary_key=True,db_column='idalumno_has_genero',default=1)
    fk_alumno = models.ForeignKey(Alumnos,on_delete=models.CASCADE,db_column='fk_alumno')
    fk_genero = models.ForeignKey(Genero,on_delete=models.CASCADE,db_column='fk_genero')
    class Meta:
        db_table='alumno_has_genero'
             
        
        

