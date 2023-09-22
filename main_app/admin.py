from django.contrib import admin

# Register your models here.
from .models import Bear, Feeding, Food

admin.site.register(Bear)
admin.site.register(Feeding)
admin.site.register(Food)