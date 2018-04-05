from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext as _
from .models import EmpresaContratante, Contratante, Musico, Produtor, Tecnico


class EmpresaContratanteForm(forms.ModelForm):
    """Form definition for Filial."""

    class Meta:
        """Meta definition for Filialform."""

        model = EmpresaContratante
        fields = '__all__'


class ContratanteForm(forms.ModelForm):
    """Form definition for Filial."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Celular1'].widget.attrs['class'] = 'myclass'

    class Meta:
        """Meta definition for Filialform."""

        model = Contratante
        fields = '__all__'


class ProdutorForm(forms.ModelForm):
    """Form definition for Filial."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Celular1'].widget.attrs['class'] = 'myclass'

    class Meta:
        """Meta definition for Filialform."""

        model = Produtor
        fields = '__all__'


class MusicoForm(forms.ModelForm):
    """Form definition for Filial."""

    class Meta:
        """Meta definition for Filialform."""

        model = Musico
        fields = '__all__'


class TecnicoForm(forms.ModelForm):
    """Form definition for Filial."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Celular1'].widget.attrs['class'] = 'myclass'

    class Meta:
        """Meta definition for Filialform."""

        model = Tecnico
        fields = '__all__'
