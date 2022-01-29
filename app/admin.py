from django.contrib import admin
from app.models import City, Attraction, Review

# Registering models here.
admin.site.register(City)
admin.site.register(Attraction)
admin.site.register(Review)
