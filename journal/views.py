from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm, EntryUpdateForm, EntryDeleteForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from langchain_google_genai import GoogleGenerativeAI
from langchain import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
google_gemini_api_key = os.getenv("GOOGLE_GEMINI_API_KEY")


@login_required
def profile(request):
    return render(request, 'journal/profile.html', {'user': request.user, 'entries': Entry.objects.filter(user=request.user)})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        entries = Entry.objects.filter(user=request.user).order_by('-id')

        # Pagination
        paginator = Paginator(entries, 5) # 5 entries per page
        page = request.GET.get('page')
        try:
            entries = paginator.page(page)
        except PageNotAnInteger:
            entries = paginator.page(1)
        except EmptyPage:
            entries = paginator.page(paginator.num_pages)

        context = {'entries': entries}
        return render(request, 'journal/dashboard.html', context)
    else:
        return redirect('login')

@login_required
def new_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()

            try:
                llm = GoogleGenerativeAI(google_api_key=google_gemini_api_key, model="gemini-1.5-flash", temperature=0)
                prompt_template = """
                Analyze the following journal entry for elements of accountability, awareness (judgement by Allah), gratitude, humility, tawakul, and identified areas for self-improvement(fahm), hassad, keena, zulm, takbur, kahali(sloth). Provide concise answers in a well-formatted HTML unordered list.

                Title: {title}
                Text: {text}

                Output should be an HTML <ul> list with <li> elements for each category. Each <li> element should start with the category name in bold, followed by a colon and the analysis. Do not use asterisks or other markdown formatting.

                """
                prompt = PromptTemplate(template=prompt_template, input_variables=["title", "text"])
                analysis = llm(prompt.format(title=entry.title, text=entry.text))
                entry.intention = analysis
                entry.save()
            except Exception as e:
                print(f"Error during LangChain analysis: {e}")

            return redirect('dashboard')
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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            gender = form.cleaned_data['gender']

            user = User.objects.create_user(username=username, password=password)
            # Optionally, add gender to the User model (requires migration)
            # user.gender = gender  # Assuming you've added a gender field to the User model
            # user.save()

            login(request, user)
            messages.success(request, "Signup successful!")
            return redirect('dashboard')  # Redirect to your dashboard
        else:
            messages.error(request, "Signup failed. Please check the form.")
    else:
        form = SignUpForm()
    return render(request, 'journal/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('dashboard') # Redirect to the dashboard after logout
