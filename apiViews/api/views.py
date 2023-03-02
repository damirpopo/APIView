from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from django.forms import model_to_dict
from .serializers import ProductSerializer

class MenAPIView(APIView):

    def get(self, request,*args,**kwargs):
        pk=kwargs.get("pk", None)
        w = Product.objects.all()
        return Response({'posts': ProductSerializer(w,many=True).data})


    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Product.objects.create(
            name=request.data['name'],
            size=request.data['size'],
            price=request.data['price'],
        )
        return Response({'post':ProductSerializer(post_new).data})

    def put(self,request,*args,**kwargs):
        pk=kwargs.get("pk", None)
        if not pk:
            return Response({"error":"PUT not allowed"})
        try:
            instance = Product.objects.get(pk=pk)
        except:
            return Response({"error": "not exists"})

        serializer= ProductSerializer(data=request.data,instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})


    def delete(self, request,*args,**kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"errors":"Метод не сработал"})

        w=Product.objects.get(pk=pk)
        w.delete()

        return Response({"post":"delete post"+ str(pk)})
