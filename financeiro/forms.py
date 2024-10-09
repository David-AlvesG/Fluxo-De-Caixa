from django import forms
from .models import Lancamento

class LancamentoForm(forms.ModelForm):
    class Meta:
        model = Lancamento
        fields = ['tipo', 'valor', 'descricao', 'data']  # Inclua 'data' aqui
