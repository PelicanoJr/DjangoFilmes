from django import forms
from filmes.models import Filme  

  
class FilmesModelForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'
        widgets = {
            'atores': forms.CheckboxSelectMultiple()   }
        
    
    def clean_ano(self):
        ano = self.cleaned_data.get('ano')
        if ano < 1900 or ano > 2100:
            self.add_error('ano', 'O ano deve estar entre 1900 e 2100.')
        return ano