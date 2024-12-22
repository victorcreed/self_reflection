from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Entry
from django.contrib.auth import authenticate, login

def dashboard(request):
    if request.user.is_authenticated:
        entries = Entry.objects.filter(user=request.user)
        return render(request, 'journal/dashboard.html', {'entries': entries})
    else:
        return redirect('login') #This assumes you have a login view set up.

@login_required
def new_entry(request):
    if request.method == 'POST':
        #Process form data here
        pass #Add form processing logic later
    return render(request, 'journal/new_entry.html')
