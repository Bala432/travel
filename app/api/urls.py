from django.urls import path
from app.api.views import ( CityCreateView, CityListView, CityRetrieveUpdateDestroyView,
                            AttractionCreateView, AttractionListView, AttractionRetrieveUpdateDestroyView )

urlpatterns = [
    path('create-city/',CityCreateView.as_view()),
    path('cities-list/',CityListView.as_view()),
    path('city/<int:pk>/',CityRetrieveUpdateDestroyView.as_view()),
    path('create-attraction/',AttractionCreateView.as_view()),
    path('city/<int:pk>/attractions',AttractionListView.as_view()),
    path('attraction/<int:pk>',AttractionRetrieveUpdateDestroyView.as_view())
]