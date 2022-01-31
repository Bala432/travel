from app.models import City, Attraction, Review
from app.api.serilaizers import CitySerializer, AttractionSerializer, ReviewSerializer, UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from app.api.throttling import AttractionListThrottle, ReviewListThrottle

# API for Login Tokens
class LoginTokenView(APIView):
    
    def post(self, request):
        
        username = request.data['username']
        password = request.data['password']
        
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError('Invalid username or password')
        account = User.objects.get(username=username)
        data = {}
        data['username'] = account.username
        data['response'] = 'Login Successful'
        refresh_token = RefreshToken.for_user(account)
        data['token'] = {
            'access_token' : str(refresh_token.access_token),
            'refresh_token' : str(refresh_token)
        }
        return Response(data)
    
# API for Registering User
class RegisterView(APIView):
    
    def post(self, request):
        
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration Succesfull'
            data['username'] = account.username
            refresh_token = RefreshToken.for_user(account)
            data['token'] = {
                'access_token': str(refresh_token.access_token),
                'refresh_token' : str(refresh_token)
            }
            
        else:
            data = serializer.errors
        return Response(data)

# API for Registering a City
class CityCreateView(CreateAPIView):
    
    # def post(self, request):
    #     city_serializer = CitySerializer(data=request.data)
    #     if city_serializer.is_valid():
    #         city_serializer.save()
    #         return Response(city_serializer.data)
    #     else:
    #         return Response(city_serializer.errors)
    
    serializer_class = CitySerializer
        
# API for Obtaining List of Cities
class CityListView(ListAPIView):
    
    # def get(self, request):
    #     cities = City.objects.all()
    #     city_serializer = CitySerializer(cities,many=True)
    #     return Response(city_serializer.data)
    
    serializer_class = CitySerializer
    queryset = City.objects.all()
    
# API for Retrieving, Updating and Deleting a Particular City
class CityRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    
    # def get(self, request, pk):
    #     try:
    #         city = City.objects.get(pk=pk)
    #     except City.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)       
    #     city_serializer = CitySerializer(city)
    #     return Response(city_serializer.data)
    
    # def put(self,request,pk):
    #     try:
    #         city = City.objects.get(pk=pk)
    #     except City.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)       
    #     city_serializer = CitySerializer(city,data=request.data)
    #     if city_serializer.is_valid():
    #         city_serializer.save()
    #         return Response(status=status.HTTP_200_OK)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
        
    # def delete(self, request,pk):
    #     try:
    #         city = City.objects.get(pk=pk)
    #     except City.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)       
    #     city.delete()
    #     return Response(status=status.HTTP_200_OK)
    
    serializer_class = CitySerializer
    queryset = City.objects.all()
    
# API for Creating Attractions
class AttractionCreateView(CreateAPIView):
    
    # def post(self,request):
    #     attraction_serializer = AttractionSerializer(data=request.data)
    #     if attraction_serializer.is_valid():
    #         attraction_serializer.save()
    #         return Response(status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    
    serializer_class = AttractionSerializer
        
# API for Retrieving list of Attractions By City
class AttractionListView(ListAPIView):
    
    # def get(self, request, pk):
    #     attractions = Attraction.objects.filter(city=pk)
    #     if attractions is None:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     attraction_serializer = AttractionSerializer(attractions,many=True)
    #     return Response(attraction_serializer.data)
    
    permission_classes = [ IsAuthenticated ]
    serializer_class = AttractionSerializer
    throttle_classes = [AttractionListThrottle]
    
    def get_queryset(self):
        print("self.kwargs is ",self.kwargs)
        print("self.request is ",self.request)
        pk = self.kwargs['pk']
        return Attraction.objects.filter(city=pk)
    
    
# API for Retrieving, Updating and Destroying a Particular Attraction
class AttractionRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    
    # def get(self, request, pk):
    #     try:
    #         attraction = Attraction.objects.get(pk=pk)
    #     except Attraction.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     attraction_serializer = AttractionSerializer(attraction)
    #     return Response(attraction_serializer.data)
    
    # def put(self, request, pk):
    #     try:
    #         attraction = Attraction.objects.get(pk=pk)
    #     except Attraction.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     attraction_serializer = AttractionSerializer(attraction,data=request.data)
    #     if attraction_serializer.is_valid():
    #         attraction_serializer.save()
    #         return Response(attraction_serializer.data)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
        
    # def delete(self, request, pk):
    #     try:
    #         attraction = Attraction.objects.get(pk=pk)
    #     except Attraction.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     attraction.delete()
    #     return Response(status=status.HTTP_200_OK)
    
    serializer_class = AttractionSerializer
    queryset = Attraction.objects.all()
    
# API for Creating Review by User
class CreateReviewView(CreateAPIView):
    
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [ IsAuthenticated ]
    
    def perform_create(self,serializer):
        
        user = self.request.user
        pk = self.kwargs['pk']
        try:
            attraction = Attraction.objects.get(pk=pk)
        except Attraction.DoesNotExist:
            raise ValidationError({'Error':'This Place does not exist'})
        
        review = Review.objects.filter(attractions=attraction,review_user=user)
        if review.exists():
            raise ValidationError({'Error':'This Place is already reviewed'})
        
        if attraction.number_of_ratings == 0:
            attraction.average_rating = serializer.validated_data['rating']
        else:
            attraction.average_rating = ( attraction.average_rating + serializer.validated_data['rating'] ) /2
        attraction.number_of_ratings = attraction.number_of_ratings + 1
        attraction.save()
        serializer.save(attractions = attraction, review_user=user)
        
# API for Listing Reviews for specific Attraction
class ReviewListView(ListAPIView):
    
    serializer_class = ReviewSerializer
    throttle_classes = [ReviewListThrottle]
    def get_queryset(self):
        pk = self.kwargs['pk']
        reviews = Review.objects.filter(attractions=pk)
        return reviews