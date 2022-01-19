from django import forms
from .modelos import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Utilizador ou password Incorretos')
            if not user.check_password(password):
                raise forms.ValidationError('Utilizador ou password Incorretos')
        return super(LoginForm, self).clean(*args, **kwargs)


class ExtendedUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)

        user.username = self.cleaned_data['username']

        if commit:
            user.save()
        return user


class UtilizadorForm(forms.ModelForm):
    class Meta:
        model = Utilizador
        fields = [
            'nome',
            'data_nascimento',
            'n_cc',
            'n_cont',
            'permissao'
        ]


class UtenteForm(forms.ModelForm):
    class Meta:
        model = Utente
        fields = [
            'id_utentes'
            'nome',
            'data_nascimento',
            'n_cc',
            'n_cont',
        ]


class MedicamentosForm(forms.ModelForm):
    class Meta:
        model = Medicamentos
        fields = '__all__'


class AdicionarConsulta(forms.Form):
    id_medico = forms.CharField(max_length=9)
    id_utente = forms.CharField(max_length=9)
    descricao = forms.CharField("Descrição da consulta", max_length=80)


class AdicionarPrescriçãoForm(forms.Form):
    id_farmaceutico = forms.CharField()
    id_utente = forms.CharField(max_length=9)
    id_medicamento = forms.CharField()




class RUtilizadorForm(forms.Form):
    name = forms.CharField(required=False)
    n_cc = forms.CharField(max_length=8, unique=True)
    n_cont = forms.CharField(max_length=9, unique=True)
    data_nascimento = forms.CharField(required=False, max_length=10)

    TYPES = [
        ('NONE', '-'),
        ('A', 'Administrador'),
        ('M', 'Medico'),
        ('F', 'Farmaceutico'),
    ]

    type = forms.ChoiceField(required=False, choices=TYPES)


class RUtenteForm(forms.Form):
    nome = forms.CharField(required=False)
    n_cc = forms.EmailField(required=False)
    data_nascimento = forms.CharField(max_length=9, required=False)
    n_cont = forms.CharField(max_length=8, required=False)



class RMedicamentoForm(forms.Form):
    descrição = forms.CharField(required=False)
    quantidade = forms.CharField(required=False)
    id_fornecedor = forms.CharField(required=False)
    quantidade_minima = forms.CharField(required=False)


class RConsultaForm(forms.Form):
    id_medico = forms.CharField(required=False)
    id_paciente = forms.CharField(max_length=9, required=False)
    descrição = forms.Charfield(max_lenght=80)



class RPrescriçãoForm(forms.Form):
    farmaceutico = forms.CharField(required=False)
    utentes = forms.CharField(max_length=9, required=False)
    id_medicamento = forms.CharField(required=False)


class UploadForm(forms.Form):
    title = forms.CharField(max_length=100)
    txt = forms.FileField()