from django import forms
from .models import Todos

class ListForm(forms.ModelForm):
    """Form definition for List."""

    class Meta:
        """Meta definition for Listform."""

        model = Todos
        fields = ["titlee","description","finished","date"]
