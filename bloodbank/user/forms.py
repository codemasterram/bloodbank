from django import forms
from .models import Bloodbank,Donors

class BloodbankForm(forms.ModelForm):

	class Meta:
		model=Bloodbank
		fields='__all__'

class DonorsForms(forms.ModelForm):

	class Meta:
		model=Donors
		fields='__all__'