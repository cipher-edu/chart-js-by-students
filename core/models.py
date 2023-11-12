from django.db import models

# Create your models here.
class Strana(models.Model):
    name = models.CharField(max_length=255, verbose_name='Davlat nomi')
    aholi_soni = models.IntegerField(verbose_name='axoli soni')

    def __str__(self):
        return self.name