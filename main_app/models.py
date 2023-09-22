from django.db import models
from django.urls import reverse


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

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
    return reverse('bears_detail', kwargs={'bear_id': self.id})
  
class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
     max_length=1,
     choices=MEALS,
     default=MEALS[0][0]
    )
  
  bear = models.ForeignKey(
     Bear,
     on_delete=models.CASCADE
    )

  def __str__(self):
     return f'{self.get_meal_display()} on {self.date}'