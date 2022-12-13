from django.urls import path  
from .views import SchoolListView
urlpatterns = [
    path('', SchoolListView.as_view(),name="school_list"),
]