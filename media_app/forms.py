from django.core.exceptions import ValidationError
from django import forms
from .models import LandLord,Tenant



class LandLordForm(forms.ModelForm):
    class Meta:
        model=LandLord
        fields="__all__"


class UploadForm(forms.Form):
    user_file=forms.ImageField()

def validate_username(value):
     if "/" in value:
            raise ValidationError("Invalid Usename.Do not use a backslash ('/')")
class TenantForm(forms.ModelForm):
    username=forms.CharField(max_length=15, validators=[validate_username])
    class Meta:
        model=Tenant
        fields='__all__'
    