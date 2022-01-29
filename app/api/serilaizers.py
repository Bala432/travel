from app.models import City, Attraction, Review
from rest_framework import serializers

# Serilaizing City Model
class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City
        fields = "__all__"
        
# Serializing Attraction Model
class AttractionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Attraction
        fields = "__all__"
        
# Serilaizing Review Model
class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = "__all__"