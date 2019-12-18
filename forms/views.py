from django.shortcuts import render
# from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def home(request):
    # my_user = User.objects.get(username='whatever')
    # profile = my_user.profile
    return render(request, "index.html")

def addProfile(request):
    return render(request, "add.html")