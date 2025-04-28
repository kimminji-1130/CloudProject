# myapp/views.py
from django.http import JsonResponse

def healthz(request):
    return JsonResponse({'status': 'ok'})

# myapp/urls.py
from django.urls import path
from .views import healthz

urlpatterns = [
    path('healthz/', healthz, name='healthz'),
]
