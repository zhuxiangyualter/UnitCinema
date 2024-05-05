from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden, FileResponse
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.db.models import Q, Count, Max, F
from datetime import timedelta
from io import BytesIO
import json
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        # confirm_password = request.data.get('confirm_password')
        # if password != confirm_password:
        #     return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
        if Worker.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        Worker.objects.create_user(username=username, password=password)
        return Response('User created successfully')

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        Worker = authenticate(request, username=username, password=password)
        if Worker is not None:
            login(request, Worker)
            token, created = Token.objects.get_or_create(user=Worker)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
    def get(self, request):
        logout(request)
        return redirect('user:login')

class UserProfileAPIView(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            return Response('User profile')
        else:
            return redirect('worker:login')
class UserProfileEditAPIView(APIView):
    def post(self, request):
        Worker = request.user
        return Response('User profile')
class UserRepwdView(APIView):
    @permission_classes([IsAuthenticated])
    def post(self, request):
        worker = request.user
        password = request.data.get('password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')
        if not worker.check_password(password):
            return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
        if new_password != confirm_password:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
        worker.set_password(new_password)
        worker.save()
        update_session_auth_hash(request, worker)
        return Response('Password updated successfully')