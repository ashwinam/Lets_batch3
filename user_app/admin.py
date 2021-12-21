from django.contrib import admin
from .models import Profile 

# Register your models here.

@admin.register(Profile )
class Profle_data(admin.ModelAdmin):
	list_display = ['age', 'image' ]