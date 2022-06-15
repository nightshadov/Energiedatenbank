from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ExperimentLog, AlmemoLog, EnYear
from .serializers import ExperimentLogSerializer, AlmemoLogSerializer, EnYearSerializer

import logging

logger = logging.getLogger(__name__)


# Create your views here.
@api_view(['GET'])
def index(request):
    api_urls = {

    }
    return Response(api_urls)

