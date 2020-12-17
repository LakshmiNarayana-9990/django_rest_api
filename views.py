from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import projectSerializer
from .models import project

class projectViewSet(viewsets.ModelViewSet):
    queryset = project.objects.all()
    serializer_class = projectSerializer
from django.http import JsonResponse

def send_json(request):

    

    return JsonResponse(projectSerializer.data, safe=False)