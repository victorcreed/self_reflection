from django import forms
from .models import Entry

class EntryUpdateForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'

class EntryDeleteForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [] # No fields needed for delete form

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__' # Include all fields from the Entry model
