# eventos/forms.py

from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descricao', 'data_hora_inicio', 'data_hora_termino', 'local']

    def clean(self):
        cleaned_data = super().clean()
        data_hora_inicio = cleaned_data.get("data_hora_inicio")
        data_hora_termino = cleaned_data.get("data_hora_termino")

        if data_hora_inicio and data_hora_termino:
            if data_hora_termino < data_hora_inicio:
                raise forms.ValidationError("A data de término deve ser posterior à data de início.")
