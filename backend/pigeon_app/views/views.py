from django.http import JsonResponse
from ..models.test import Test

def index(request):
    return JsonResponse({ "status": "I'm here" })