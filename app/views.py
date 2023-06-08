from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def EmpMSjsonData(request):
    EQS=Employee.objects.all()
    ESD=EmpModelSerializers(EQS,many=True)
    return Response(ESD.data)