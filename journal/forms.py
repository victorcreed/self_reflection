from django import forms
from .models import Entry

class EntryUpdateForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text', 'intention']

class EntryDeleteForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [] # No fields needed for delete form

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text', 'intention']
