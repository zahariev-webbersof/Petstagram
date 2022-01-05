from django import forms

from Petstagram.core.forms import BootstrapFormMixin
from Petstagram.pets.models import Pet


class PetForm(BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'some-class',
                }
            )
        }


class EditPetForm(PetForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }