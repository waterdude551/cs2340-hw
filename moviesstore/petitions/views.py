from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Petition

# Create your views here.

def index(request):
    petitions = Petition.objects.all()
    return render(request, 'petitions/index.html', {'petitions': petitions})

def create_petition_screen(request):
    return render(request, 'petitions/create_petition.html')


@login_required


@login_required
def create_petition(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        if title:
            petition = Petition()
            petition.title = title
            petition.description = description
            petition.score = 1
            petition.save()  # Save first to get an ID
            petition.voters.add(request.user)
            petition.save()
            return redirect('petitions.index')
        else:
            error = 'Title is required.'
            return render(request, 'petitions/create_petition.html', {'error': error, 'title': title, 'description': description})
    else:
        return render(request, 'petitions/create_petition.html')

@login_required
def vote(request, id):
    petition = Petition.objects.get(id=id)
    petition.voters.add(request.user)
    petition.score += 1
    petition.save()
    return redirect('petitions.index')

@login_required

@login_required
def unvote(request, id):
    petition = Petition.objects.get(id=id)
    petition.voters.remove(request.user)
    petition.score -= 1
    petition.save()
    return redirect('petitions.index')