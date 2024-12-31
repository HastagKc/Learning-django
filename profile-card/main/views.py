from django.shortcuts import render
from .models import Profile

# Create your views here.


def home(request):
    # Querysets
    profiles = Profile.objects.all()
    print(profiles)
    context = {'profiles': profiles}
    return render(request, 'main/index.html', context)


def single_profile(request, pk):
    # fetching single data
    profile = Profile.objects.get(pk=pk)
    print(profile)
    context = {'profile': profile}
    return render(request, 'main/profile.html', context)
