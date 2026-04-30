"""Plantilla de `forms.py` con un `ModelForm` de ejemplo.

No incluye lógica; completar cuando se implemente `models.Calificacion`.
"""

from django import forms

from .models import Calificacion


class CalificacionForm(forms.ModelForm):
	class Meta:
		model = Calificacion
		exclude = ['promedio']


