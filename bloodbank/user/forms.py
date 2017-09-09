from django import forms
from .models import Bloodbank

class BloodbankForm(forms.ModelForm):

	class Meta:
		model=Bloodbank
		fields='__all__'