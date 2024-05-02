from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from user.models import User  # 确保从你的 models.py 中导入 User
from django.http.request import HttpRequest
from worker.models import Worker
@login_required(login_url='user:login')
def user(request):
    if not request.user.is_staff:
        return HttpResponse('403 Forbidden', status=403)

    if request.method == 'GET':
        users = User.objects.all()
        return HttpResponse('admin/manage_users.html', {
            'users': users
        })
    elif request.method == 'POST':
        if 'delete' in request.POST:
            user = User.objects.get(id=request.POST.get('id'))
            user.delete()
            return HttpResponse('User deleted successfully!')
        elif 'toggle_active' in request.POST:
            user = User.objects.get(id=request.POST.get('id'))
            user.is_active = not user.is_active
            user.save()
            return HttpResponse('User activation status changed!')
        else:
            return HttpResponseBadRequest('Invalid request')


@login_required(login_url='user:login')
def worker(request):
    if not request.user.is_staff:
        return HttpResponse('403 Forbidden', status=403)

    if request.method == 'GET':
        workers = Worker.objects.all()
        return HttpResponse('admin/manage_workers.html', {
            'workers': workers
        })
    elif request.method == 'POST':
        if 'delete' in request.POST:
            worker = Worker.objects.get(id=request.POST.get('id'))
            worker.delete()
            return HttpResponse('Worker deleted successfully!')
        elif 'toggle_active' in request.POST:
            worker = Worker.objects.get(id=request.POST.get('id'))
            worker.is_active = not worker.is_active
            worker.save()
            return HttpResponse('Worker activation status changed!')
        else:
            return HttpResponseBadRequest('Invalid request')