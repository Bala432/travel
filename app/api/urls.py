from django.urls import path
from app.api.views import ( CityCreateView, CityListView, CityRetrieveUpdateDestroyView,
                            AttractionCreateView, AttractionListView, AttractionRetrieveUpdateDestroyView,
                            LoginTokenView, RegisterView, CreateReviewView, ReviewListView)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('create-city/',CityCreateView.as_view()),
    path('cities-list/',CityListView.as_view()),
    path('city/<int:pk>/',CityRetrieveUpdateDestroyView.as_view()),
    path('create-attraction/',AttractionCreateView.as_view()),
    path('city/<int:pk>/attractions',AttractionListView.as_view()),
    path('attraction/<int:pk>/',AttractionRetrieveUpdateDestroyView.as_view()),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
    path('login/',LoginTokenView.as_view()),
    path('register/',RegisterView.as_view()),
    path('attraction/<int:pk>/create-review', CreateReviewView.as_view()),
    path('attraction/<int:pk>/reviews',ReviewListView.as_view())
]