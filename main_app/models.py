from django.db import models
from django.urls import reverse

# Create your models here.
class Bear(models.Model):
  species = models.CharField(max_length=100)
  latin_name = models.CharField(max_length=100)
  weight_bottom = models.IntegerField(blank=True, null=True)
  weight_top = models.IntegerField()
  size = models.CharField(max_length=100)
  color = models.CharField(max_length=100)

  def __str__(self):
        return f'{self.species}'
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'bear_id': self.id})
  
