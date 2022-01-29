from app.models import City, Attraction, Review
from app.api.serilaizers import CitySerializer, AttractionSerializer, ReviewSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# API for Registering a City
class CityCreateView(APIView):
    
    def post(self, request):
        city_serializer = CitySerializer(data=request.data)
        if city_serializer.is_valid():
            city_serializer.save()
            return Response(city_serializer.data)
        else:
            return Response(city_serializer.errors)
        
# API for Obtaining List of Cities
class CityListView(APIView):
    
    def get(self, request):
        cities = City.objects.all()
        city_serializer = CitySerializer(cities,many=True)
        return Response(city_serializer.data)
    
# API for Retrieving, Updating and Deleting a Particular City
class CityRetrieveUpdateDestroyView(APIView):
    
    def get(self, request, pk):
        try:
            city = City.objects.get(pk=pk)
        except City.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)       
        city_serializer = CitySerializer(city)
        return Response(city_serializer.data)
    
    def put(self,request,pk):
        try:
            city = City.objects.get(pk=pk)
        except City.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)       
        city_serializer = CitySerializer(city,data=request.data)
        if city_serializer.is_valid():
            city_serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,pk):
        try:
            city = City.objects.get(pk=pk)
        except City.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)       
        city.delete()
        return Response(status=status.HTTP_200_OK)
    
# API for Creating Attractions
class AttractionCreateView(APIView):
    
    def post(self,request):
        attraction_serializer = AttractionSerializer(data=request.data)
        if attraction_serializer.is_valid():
            attraction_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
# API for Retrieving list of Attractions By City
class AttractionListView(APIView):
    
    def get(self, request, pk):
        attractions = Attraction.objects.filter(city=pk)
        if attractions is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        attraction_serializer = AttractionSerializer(attractions,many=True)
        return Response(attraction_serializer.data)
    
# API for Retrieving, Updating and Destroying a Particular Attraction
class AttractionRetrieveUpdateDestroyView(APIView):
    
    def get(self, request, pk):
        try:
            attraction = Attraction.objects.get(pk=pk)
        except Attraction.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        attraction_serializer = AttractionSerializer(attraction)
        return Response(attraction_serializer.data)
    
    def put(self, request, pk):
        try:
            attraction = Attraction.objects.get(pk=pk)
        except Attraction.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        attraction_serializer = AttractionSerializer(attraction,data=request.data)
        if attraction_serializer.is_valid():
            attraction_serializer.save()
            return Response(attraction_serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            attraction = Attraction.objects.get(pk=pk)
        except Attraction.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        attraction.delete()
        return Response(status=status.HTTP_200_OK)