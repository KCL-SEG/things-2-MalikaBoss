"""Forms of the project."""
from django import forms
from things.models import Thing

# Create your forms here.
class ThingForm(forms.ModelForm):
    description = forms.CharField(max_length=120, widget = forms.Textarea)
    
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
