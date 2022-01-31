from app.models import City, Attraction, Review
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

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
        
    def to_representation(self, instance ):
        print("instance is ", instance)
        data = {}
        data['name'] = instance.name
        data['type_of_place'] = instance.type_of_place
        
        is_ticket_required = instance.is_ticket_required
        if is_ticket_required:
            data['tickets'] = 'Required'
            data['adult_ticket'] = instance.adult_ticket
            data['child_ticket'] = instance.child_ticket
        else:
            data['tickets'] = 'Not Required'
        
        number_of_ratings = instance.number_of_ratings
        if number_of_ratings == 0 :
            data['Ratings'] = 'No one has rated this place'
        else:
            data['Ratings'] = number_of_ratings
            data['average_rating'] = instance.average_rating
            
        data['city'] = instance.city.name
        return data
        
        
# Serilaizing Review Model
class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = ('comment','rating','review_user')
        
# Serializing User Model
class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=30,write_only=True,
                                      style={'input_type':'password'})
    class Meta:
        model = User
        fields = ('username','email', 'password', 'password2')
        extra_kwargs = {
            'password' : {'write_only' : True }
        }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        username = self.validated_data['username']
        email = self.validated_data['email']
        
        if password != password2 :
            raise ValidationError({'Error':"Both Passwords didn't match"})
        
        if User.objects.filter(username=username).exists():
            raise ValidationError({'Error':'This Userrname already Exist'})
        
        if User.objects.filter(email=email).exists():
            raise ValidationError({'Error':'Email is already registered'})
        
        account = User(email=email,username=username)
        account.set_password(password)
        account.save()
        return account