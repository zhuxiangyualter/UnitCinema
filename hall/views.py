from django.http import HttpResponse
from .models import Hall
from django.shortcuts import get_object_or_404
def hall(request):
    halls = Hall.objects.all()
    hall_list = ", ".join([hall.name for hall in halls])
    return HttpResponse(f"Halls available: {hall_list}")
def hall_detail(request, hall_id):
    hall = get_object_or_404(Hall, pk=hall_id)
    hall_details = f"Name: {hall.name}, Capacity: {hall.capacity}"
    return HttpResponse(f"Hall Details: {hall_details}")