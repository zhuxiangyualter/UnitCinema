from django.http import HttpResponse
from rest_framework import status

from .models import Film
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Film
from .models import FilmSerializer
class FilmListAPIView(APIView):
    def get(self, request, format=None):
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)
class FilmDetailAPIView(APIView):
    def get(self, request, film_id, format=None):
        film = get_object_or_404(Film, pk=film_id)
        serializer = FilmSerializer(film)
        return Response(serializer.data)
class FilmCreateAPIView(APIView):
     def post(self, request, format=None):
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class FilmDeleteAPIView(APIView):
    def post(self, request, film_id, format=None):
        film = get_object_or_404(Film, pk=film_id)
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class FilmUpdateAPIView(APIView):
    def post(self, request, format=None):
        # 从POST数据中获取film_id
        film_id = request.data.get('fno')
        if not film_id:
            return Response({"error": "Missing film_id"}, status=status.HTTP_400_BAD_REQUEST)

        film = get_object_or_404(Film, pk=film_id)
        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)