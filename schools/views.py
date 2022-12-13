from django.shortcuts import render
from .serializers  import SchoolSerializer
from .models import School
from rest_framework.generics import ListAPIView ,ListCreateAPIView, RetrieveAPIView , RetrieveUpdateAPIView , RetrieveUpdateDestroyAPIView

# Create your views here.
class SchoolListView(ListCreateAPIView):
    # I want to show user the data and can create another data from list
    queryset = School.objects.all() # take all object and give him to serilizer
    serializer_class = SchoolSerializer # afile resposible to convert python code to JSON data/ format

# class SchoolListView(ListAPIView):
#     # I want to show user the data
#     queryset = School.objects.all() 
#     serializer_class = SchoolSerializer 

class SchooleDetailView(RetrieveUpdateDestroyAPIView):

    # RetrieveUpdateDestroyAPIView : mean reading , can Updating and delet
    queryset = School.objects.all() 
    serializer_class = SchoolSerializer 

# class SchooleDetailView(RetrieveUpdateAPIView):

#     # RetrieveUpdateAPIView : mean reading and can editing
#     queryset = School.objects.all() 
#     serializer_class = SchoolSerializer 

# class SchooleDetailView(RetrieveAPIView):

#     # RetrieveAPIView : mean just reading the data
#     queryset = School.objects.all() 
#     serializer_class = SchoolSerializer 
