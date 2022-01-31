from django.contrib import admin
from .models import Fruit, Region

# Register your models here.
admin.site.register(Region)
@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ("name", "region_id")
