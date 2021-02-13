from django.shortcuts import render
from Meme.models import Meme

# Create your views here.
def index(request):
    memes=Meme.objects.all()[:100]
    
    context={
        'memes':memes,
    }
    
    return render(request, 'frontend/index.html', context)