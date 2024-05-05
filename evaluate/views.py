
from .models import *
from django.db.models import Q, Count, Max, F
from datetime import timedelta
from io import BytesIO
import json
from django.utils.timezone import now
from django.shortcuts import get_object_or_404, render
from .models import Evaluate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class EvaluateListView(APIView):
    def get(self, request, *args, **kwargs):
        evaluates = Evaluate.objects.all()
        serializer = EvaSerializer(evaluates, many=True)
        return Response(serializer.data)
class EvaluateDetailView(APIView):
    def get(self, request, cno, fno, *args, **kwargs):
        evaluate = get_object_or_404(Evaluate, cno=cno, fno=fno)
        serializer = EvaSerializer(evaluate)
        return Response(serializer.data)
class EvaluateCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EvaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class EvaluateDeleteView(APIView):
    def delete(self, request, cno, fno, *args, **kwargs):
        evaluate = get_object_or_404(Evaluate, cno=cno, fno=fno)
        evaluate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
