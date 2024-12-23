from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm, EntryUpdateForm, EntryDeleteForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

@login_required
def profile(request):
    return render(request, 'journal/profile.html', {'user': request.user, 'entries': Entry.objects.filter(user=request.user)})

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

@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id, user=request.user)
    if request.method == 'POST':
        form = EntryUpdateForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EntryUpdateForm(instance=entry)
    return render(request, 'journal/edit_entry.html', {'form': form, 'entry': entry})

@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id, user=request.user)
    if request.method == 'POST':
        form = EntryDeleteForm(request.POST, instance=entry)
        entry.delete()
        return redirect('profile')
    else:
        form = EntryDeleteForm(instance=entry)
    return render(request, 'journal/delete_entry.html', {'form': form, 'entry': entry})

def logout_view(request):
    logout(request)
    return redirect('dashboard') # Redirect to the dashboard after logout
