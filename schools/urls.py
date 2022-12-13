from django.urls import path  # 1. import any thing built in django
from .views import SchoolListView
urlpatterns = [
    path('', SchoolListView.as_view(),name="school_list"),
]