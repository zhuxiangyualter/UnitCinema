from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Ticket

def buyticket(request):
    # This is a simplified view that might use GET parameters to simulate ticket buying
    if request.method == 'POST':
        # Simulate ticket buying logic
        event_id = request.POST.get('event_id')
        user_id = request.POST.get('user_id')
        # Assume Ticket model has 'event_id' and 'user_id'
        ticket = Ticket.objects.create(event_id=event_id, user_id=user_id)
        return redirect('ticket_detail', ticket_id=ticket.id)
    return render(request, 'tickets/buy_ticket.html')

def cancelticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == 'POST':
        # Assume cancellation is a POST action to prevent accidental deletes
        ticket.delete()
        return HttpResponse("Ticket cancelled successfully.")
    # If not POST, show some confirmation page or similar
    return render(request, 'tickets/cancel_ticket.html', {'ticket': ticket})
