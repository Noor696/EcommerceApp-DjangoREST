from rest_framework import serializers
from .models import School

class SchoolSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= School
        # fields=['id','name', 'owner', 'city', 'img_url'] # I can specific any field from model
        fields='__all__'