from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm, EntryUpdateForm, EntryDeleteForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from langchain.llms import GoogleGemini
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv                                                                                                                                                                                                                                                                                                                                             
import os
                                                                                                                                                                            
load_dotenv()                                                                                                                                                                     
google_gemini_api_key = os.getenv("GOOGLE_GEMINI_API_KEY")                                                                                                                                


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

            # LangChain integration using PromptTemplate
            llm = GoogleGemini(google_api_key=os.getenv("GOOGLE_GEMINI_API_KEY"), model="gemini-1.5-flash", temperature=0) #Get API key from environment variable

            prompt_template = """
            Analyze the following journal entry for elements of accountability, awareness, gratitude, humility, tawakul, and identified areas for self-improvement.  Provide concise answers.

            Title: {title}
            Text: {text}

            Accountability (element of justice): Does the entry show accountability?
            Awareness (judgement by Allah): Is there awareness of Allah's judgement?
            Gratitude (ihsan): Does the entry express gratitude to Allah?
            Humility (haqeeqi humility): Does the entry violate haqeeqi humility?
            Tawakul (patience): Does the entry show a lack of patience (and thus lack of tawakul)?
            Improvement: Does the entry identify areas for self-improvement?
            """
            prompt = PromptTemplate(template=prompt_template, input_variables=["title", "text"])
            chain = LLMChain(llm=llm, prompt=prompt)
            analysis = chain.run(title=entry.title, text=entry.text)
 
            entry.intention = analysis #Save the analysis to the intention field
            entry.save()
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

def logout_view(request):
    logout(request)
    return redirect('dashboard') # Redirect to the dashboard after logout
