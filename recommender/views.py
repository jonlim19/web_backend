from django.shortcuts import render
from .models import University

# Create your views here.
def index(request):
    all_uni = University.objects.all
    # return render(request,'authentication/index.html')
    return render(request,'authentication/index.html', {'all':all_uni})
