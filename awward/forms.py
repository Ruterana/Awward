# from .models import Profile
# from django import forms

# class NewProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ['user'] 
from .models import Profile,Project
from django import forms
class NewpostForm(forms.ModelForm):
    class Meta:
        model =Project
        exclude = [' project_title']
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']      