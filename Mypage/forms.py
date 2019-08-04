from django import forms
from .models import Blood

class BloodForm(forms.ModelForm):
    class Meta:
        model = Blood
        fields = ('barcode_data', 'barcode_type', )