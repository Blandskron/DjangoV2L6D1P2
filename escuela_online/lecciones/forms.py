from django import forms
from .models import Leccion

class LeccionForm(forms.ModelForm):
    class Meta:
        model = Leccion
        fields = ['nombre', 'duracion_video', 'imagen']
        