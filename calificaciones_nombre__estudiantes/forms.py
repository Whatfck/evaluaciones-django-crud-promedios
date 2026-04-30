from django import forms


class CalificacionForm(forms.ModelForm):
	class Meta:
		model = Calificacion
		exclude = ['promedio']
