from django.http import HttpResponse
from decouple import config

def hola(request):
    return HttpResponse(config('AUTENTICA_GOOGLE'))

