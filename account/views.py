from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView


class RegistrationView(APIView):
    def post(self, request):
        serializers = RegistrationSerializers