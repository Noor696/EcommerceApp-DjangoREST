from django.urls import path  
from .views import SchoolListView , SchooleDetailView  

urlpatterns = [
    path('', SchoolListView.as_view(),name="school_list"),
    path('<int:pk>', SchooleDetailView.as_view(),name='school_detail')
]

#SchooleDetailView