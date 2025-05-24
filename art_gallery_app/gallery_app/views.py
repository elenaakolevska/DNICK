from django.shortcuts import render
from .models import Artwork
from datetime import datetime
# Create your views here.

def index(request):
    # Show flights in the past
    arts = Artwork.objects.all()
    context = {'art_list': arts, 'app_name': 'ArtApp'}
    return render(request, 'index.html', context)
