from django import forms
from .models import LandLord

class LandLordForm(forms.ModelForm):
    class Meta:
        model=LandLord
        fields="__all__"


class UploadForm(forms.Form):
    user_file=forms.ImageField()
    