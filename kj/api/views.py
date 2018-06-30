from django.shortcuts import render

# Create your views here.

# Create your models here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
@csrf_exempt
def handle_incoming_video(request):

    print(str(request))
    print ("OK Ok Ok")
    return Response({"test": 'abc'})
