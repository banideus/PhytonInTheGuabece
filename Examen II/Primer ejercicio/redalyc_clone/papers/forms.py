from django import forms

class subirTrabajo(forms.Form):
	titulo= forms.CharField(max_length=40)
	autor=forms.CharField(max_length=40)
	categorias=(('CC','Ciencias Computacionales'),
		('CT','Ciencias de la Tierra'),('CN','Ciencias Naturales'),
		('CS','Ciencias Sociales'),('CM','Ciencias Medicas'))
	categoria=forms.ChoiceField(choices=categorias)
	docfile=forms.FileField(
			label='Selecciona un archivo')
