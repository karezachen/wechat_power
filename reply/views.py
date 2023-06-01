from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib

@csrf_exempt
def index(request):
    
    data = request.POST
    print(data)

    return 'success'

