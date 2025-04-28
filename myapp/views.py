from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello Django")

from django.http import JsonResponse

def healthz(request):
    return JsonResponse({"status": "ok"})
