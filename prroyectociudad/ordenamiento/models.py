from django.db import models

class Parroquia(models.Model):
    class Meta:
        ordering = ["tipo","nombre"]
        verbose_name_plural = "Las Parroquias"
    
    nombre = models.CharField("Nombre de parroquia", max_length=40)
    opciones_tipo = (
        ('urbana', 'urbana'),
        ('rural', 'rural')
        )
    tipo = models.CharField("Tipo de parroquia", max_length=6, \
            choices=opciones_tipo)

    def __str__(self):
        return "%s - %s" % (self.nombre,self.tipo )

class Barrio(models.Model):
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Los Barrios"
    nombre = models.CharField("Nombre de barrio", max_length=40)
    numViviendas = models.IntegerField("Numero de viviendas")
    opciones_numParques = (
        (1, 'Uno'),
        (2, 'Dos'),
        (3, 'Tres'),
        (4, 'Cuatro'),
        (5, 'Cinco'),
        (6, 'Sexto'),
        )
    numParques = models.IntegerField("Numero de parques", choices=opciones_numParques)
    numEdificios = models.IntegerField("Numero de edificios")
    parroquia = models.ForeignKey(Parroquia, related_name='lasparroquias', 
            on_delete=models.CASCADE)

    def __str__(self):
        return "Barrio: %s - %d - %d - %d - Parroquia(%s)" % (self.nombre, 
        self.numViviendas, self.numParques, self.numEdificios,
        self.parroquia.nombre)

