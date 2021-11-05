from django import forms
from .models import Avaliacao, Filme


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nome_completo', 'email', 'avaliacao', 'comentario']

    def __init__(self, *args, **kwargs):
        super(AvaliacaoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
