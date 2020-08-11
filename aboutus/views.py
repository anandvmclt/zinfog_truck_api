from django.shortcuts import render
from django.utils.decorators import method_decorator

from .models import AboutUs
# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from .serializer import AboutSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class AboutAPIView(APIView):

    parser_classes = (JSONParser,)
    def get(self, request):
        posts = AboutUs.objects.all()
        serializer = AboutSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AboutSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return HttpResponse("Welcome to Zinfog API testing")

def home(request):
    return render(request, "home.html")