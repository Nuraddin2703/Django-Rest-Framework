from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Teammate
from .serializers import TeammateSerializer

import requests
from googletrans import Translator


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
            return Response({"error": 'Object does not exist'})

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


class QuoteAPIView(APIView):
    def get(self, request):
        count = request.query_params.get('count', 1)
        quotes = self.get_quotes(count)
        return Response({'quotes': quotes})

    def translate_to_russian(self, text):
        translator = Translator()
        translated_text = translator.translate(text, src='en', dest='ru').text
        return translated_text

    def get_quotes(self, count):
        quotes = []
        for _ in range(count):
            quote = self.get_quote()
            quotes.append(quote)
        return quotes

    def get_quote(self):
        url = 'https://favqs.com/api/'
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = response.json()
                quote_text = data['quote']['body']
                translated_quote_text = self.translate_to_russian(quote_text)
                return {'quote': translated_quote_text}
            except (KeyError, ValueError):
                pass  # Handle incorrect format or missing keys
        return {'error': 'Failed to fetch quote'}

