from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import EnYear
from .serializers import EnYearSerializer

import logging

logger = logging.getLogger(__name__)


# Create your views here.
@api_view(['GET'])
def index(request):
    api_urls = {

    }
    return Response(api_urls)


@api_view(['POST'])
def newEnYear(request):
    serializer = EnYearSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        logger.error('POST request was not valid and was therefore not saved in database. Did you set all fields?')
        logger.error(serializer.errors)

    return Response(serializer.data)
