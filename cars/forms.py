from django import forms
from cars.models import Car, Brand
    
class CarModelForm(forms.ModelForm): # Usando ModelForm para simplificar o formulário
    class Meta:
        model = Car
        fields = '__all__'  # Inclui todos os campos do modelo Car

    def clean_value(self): # Toda validação personalizada deve ser feita em métodos que começam com 'clean_'
        value = self.cleaned_data.get('value') # Obtendo o valor do campo 'value'
        if value is not None and value < 20000:
            self.add_error('value', "Valor mínimo do carro deve ser de R$20.000,00.")
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year is not None and factory_year < 1975:
            self.add_error('factory_year', "Não é possível cadastrar carros fabricados antes de 1975.")
        return factory_year



