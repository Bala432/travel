from django.db import models

#Designing Model for a City
class City(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    tagline = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name + ' - ' + self.tagline + ' Welcomes You'
    
# Designing Model for Attractions for each City 
class Attraction(models.Model):
    name = models.CharField(max_length=50)
    type_of_place = models.CharField(max_length=50)
    is_ticket_required = models.BooleanField(default=False)
    adult_ticket = models.PositiveIntegerField(default=0)
    child_ticket = models.PositiveIntegerField(default=0)
    number_of_ratings = models.PositiveIntegerField(default=0)
    average_rating = models.FloatField(default=0)
    city = models.ForeignKey(City,on_delete=models.CASCADE,related_name='attractions')
    
    def __str__(self):
        return self.name + ' has ' + str(self.average_rating) + ' by ' + str(self.number_of_ratings)
    
# Designing Model for Review of each Attraction
class Review(models.Model):
    comment = models.TextField(max_length=255)
    rating = models.PositiveIntegerField(default=0)
    attractions = models.ForeignKey(Attraction,on_delete=models.PROTECT,related_name='reviews')
    
    def __str__(self):
        return self.comment