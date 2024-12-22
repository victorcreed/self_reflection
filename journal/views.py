from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm
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
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('dashboard') # Redirect to dashboard after saving
    else:
        form = EntryForm()
    return render(request, 'journal/new_entry.html', {'form': form})
