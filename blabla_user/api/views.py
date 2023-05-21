from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.response import Response

from .serializers import SignupSerializer


@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    user_data = SignupSerializer(user).data
    return Response(user_data)
