from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context={
        'name': 'sifat niloy',
        'age': 25, 
        'nationality':'Bangladeshi'
    }
    return render(request, "index.html",context)