from django import forms
from .models import Watch

class WatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ['title', 'brand', 'price', 'description']

    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("Soat nomi kamida 3 ta harfdan iborat bo'lishi kerak!")
        return title

   
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError("Soat narxi 0 dan baland bo'lishi shart!")
        return price