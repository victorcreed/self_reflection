from django import forms
from .models import Entry
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150, help_text="Please remember your username, as password recovery via email is not available.")
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    gender = forms.ChoiceField(choices=[('', 'Select Gender'), ('Male', 'Male'), ('Female', 'Female')], required=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")
        if password != password_confirmation:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class EntryUpdateForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text']

class EntryDeleteForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [] # No fields needed for delete form

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text']
