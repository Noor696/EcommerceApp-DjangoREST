from django.shortcuts import render
from .serializers  import SchoolSerializer
from .models import School
from rest_framework.generics import ListAPIView

# Create your views here.
class SchoolListView(ListAPIView):
    # I want to show user the data
    queryset = School.objects.all() # take all object and give him to serilizer
    serializer_class = SchoolSerializer # afile resposible to convert python code to JSON data/ format
