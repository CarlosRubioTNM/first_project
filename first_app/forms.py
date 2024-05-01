from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("El nombre debe comenzar con z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, 
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    #Añadir clean method para validar de bots
    #def clean_botcatcher(self):
    #    botcatcher = self.cleaned_data['botcatcher']
    #    if len(botcatcher) > 0:
    #        raise forms.ValidationError("Ese mi EL BOT")
    #    return botcatcher
    
    #Puedes añadir clean para todo
    def clean(self):
        cleaned_data = super().clean()


