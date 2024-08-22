from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from calendario.models import atividades
from .models import Squad
from django import forms
from .models import FreezingPeriod

class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
	def clean_email(self):
		email = self.cleaned_data['email']

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Email ja esta registrado')
		return email


class AtividadesForm(ModelForm):
    titulo = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 100}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))

    class Meta:
        model  = atividades
        fields = ["titulo", "descricao", "area", "data", "hora"]
        labels = {
            'titulo': 'Título do Evento',
            'descricao': 'Descrição do Evento',
            'area': 'Squad',
            'data': 'Data do Evento',
            'hora': 'Hora do Evento',
        }
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

class SquadForm(forms.ModelForm):
    class Meta:
        model = Squad
        fields = ['nome', 'cor']
        widgets = {
            'cor': forms.TextInput(attrs={'type': 'color'}),
        }

class FreezingPeriodForm(forms.ModelForm):
    class Meta:
        model = FreezingPeriod
        fields = ['start_date', 'end_date', 'environment', 'color']
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'environment': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
        }


