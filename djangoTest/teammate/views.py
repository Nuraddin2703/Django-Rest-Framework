from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from teammate.models import Teammate
from .serializers import TeammateSerializer


class TeammateAPIView(APIView):
    def get(self, request):
        lst = Teammate.objects.all()
        return Response({'posts': TeammateSerializer(lst, many=True).data})

    def post(self, request):
        serializer = TeammateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method put is not allowed"})
        try:
            instance = Teammate.objects.get(pk=pk)
        except:
            return Response({"post": serializer.data})

        serializer = TeammateSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Primary key (pk) not provided"})

        try:
            teammate = Teammate.objects.get(pk=pk)
        except Teammate.DoesNotExist:
            return Response({"error": "Teammate with the given pk does not exist"})

        teammate.delete()
        return Response({"success": f"Teammate with pk {pk} has been deleted"})

