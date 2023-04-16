from django import forms
from .models import Trade


class TickerForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = '__all__'
