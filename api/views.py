from django.shortcuts import render
from rest_framework.views import APIView
from api.serializers import UserSerializer,PhoneSerializer
from rest_framework.response import Response

from api.models import Phonemodel

from rest_framework.viewsets import ViewSet

# Create your views here.

class SignUpView(APIView):
   def post(self,request,*args,**kwargs):
       serializer=UserSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(data=serializer.data)
       else:
           return Response(data=serializer.errors)
       
    #list
   def get(self,request,*args,**kwargs):
       qs=Phonemodel.objects.all()
       serializer=PhoneSerializer(qs,many=True)
       return Response(data=serializer.data)
   
class MobileViewset(ViewSet):
    
    def list(self,request,*args,**kwargs):
        qs=Phonemodel.objects.all()
        deserializer=PhoneSerializer(qs,many=True)
        return Response(data=deserializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=PhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Phonemodel.objects.get(id=id)
        deserialization=PhoneSerializer(qs)
        return Response(data=deserialization.data)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        mobile_obj=Phonemodel.objects.get(id=id)
        serializer=PhoneSerializer(data=request.data,instance=mobile_obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Phonemodel.objects.get(id=id).delete()
        return Response(data={"message":"deleted"})