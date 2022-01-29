from django.contrib import admin
from app.models import City, Attractions, Review

# Registering models here.
admin.site.register(City)
admin.site.register(Attractions)
admin.site.register(Review)
