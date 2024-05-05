from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from .models import Notice
from .models import NoticeSerializer
class NoticeListView(APIView):
    def get(self, request, *args, **kwargs):
        notices = Notice.objects.all()
        serializer = NoticeSerializer(notices, many=True)
        return Response(serializer.data)
class NoticeDetailView(APIView):
    def get(self, request, notice_id, *args, **kwargs):
        notice = get_object_or_404(Notice, pk=notice_id)
        serializer = NoticeSerializer(notice)
        return Response(serializer.data)
class NoticeCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoticeDeleteView(APIView):
    def delete(self, request, notice_id, *args, **kwargs):
        notice = get_object_or_404(Notice, pk=notice_id)
        notice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
