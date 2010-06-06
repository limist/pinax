from django import forms

from pinax.apps.basic_profiles.models import Profile



class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        exclude = ["user"]
